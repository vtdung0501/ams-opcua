from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyqtgraph as pg
import sys
import traceback

import time
from opcua import ua
import opcua
import csv
import pandas as pd
from datetime import datetime

import opcua_interface


# -*- coding: utf-8 -*-

# Resource object code
#
# Created by: The Resource Compiler for PyQt5 (Qt v5.15.2)
#
# WARNING! All changes made in this file will be lost!



class WorkerSignals(QObject):
    # Lấy tín hiệu từ luồng worker

    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)

class  Worker(QRunnable):
    # Tạo class Worker kế thừa từ class QRunnable để thiết lập luồng xử lý tín hiệu và kết thúc
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        self.kwargs['progress_callback'] = self.signals.progress
    @pyqtSlot()
    def run(self):
        # Khởi tạo hàm chạy. Các hàm cần thực thi ở luồng worker sẽ chạy ở hàm này
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()

class MainWindow(QMainWindow, opcua_interface.Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.threadpool = QThreadPool()
        
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_barchart)
        self.timer.start()
          
        self.btn_connect.clicked.connect(self.connect_opc_server) # click các button để thực thi các function tương ứng
        self.btn_connect.clicked.connect(self.link_slot)
                     
        self.cb_remember.toggled.connect(self.remeber_information)
        self.btn_disconnect.clicked.connect(self.disconnect_opc_server)

        self.btn_operation.clicked.connect(self.operation_mode)
        self.btn_standby.clicked.connect(self.standby_mode)
        self.btn_Isolation.clicked.connect(self.isolation_mode)
        
# Khởi tạo dữ liệu trục x, y cho các biểu
        self.x_time = [0]
        self.y_pressure = [0]
        self.y_instantflow = [0]
        self.y_accumflow = [0]
        self.y_temp = [0]
        self.accumflow_operation = [0]
        self.accumflow_standby =[0]
        self.flow_saving = [0]
# Khởi tạo màu cho các đường thể hiện dữ liệu
        pen_1 = pg.mkPen(color=(128, 255, 0),width = 2)
        pen_2 = pg.mkPen(color=(0, 0, 255), width = 2)
        pen_3 = pg.mkPen(color=(0, 128, 255), width = 2)
        pen_4 = pg.mkPen(color=(255, 0, 0), width = 2)
# Khởi tạo các biểu đồ tương ứng
        self.data_pressure = self.graphicsView_pressure.plot(self.x_time, self.y_pressure,pen=pen_1,name = "Pressure (Kpa)")
        self.data_instantflow = self.graphicsView_intansflow.plot(self.x_time, self.y_instantflow,pen=pen_2,name = "Flow rate (L/min)")
        self.data_temp = self.graphicsView_temp.plot(self.x_time, self.y_temp,pen=pen_4, name = "Temperatue (°C)")
        self.data_accumflow = self.graphicsView_accumflow.plot(self.x_time, self.y_accumflow,pen=pen_3 ,name = "Accumulation (L)")
# Lấy thông tin đăng nhập
        try:
            self.get_info()
            
        except:
            pass

        
    def connect_opc_server(self):
        # Khởi tạo giá trị để kết nối tới server
        url = self.le_url.text()
        username = self.le_username.text()
        password = self.le_password.text()
        global client
        client = opcua.Client(url, timeout=60)
        client.set_user(username)
        client.set_password(password)

        try:
            client.connect()
            client.open_secure_channel(renew=True)
            self.lb_status.setText("Status: Connected.")     
        except Exception:
            self.messege_box_warning()
        
        
        
    def get_data(self, **kargs):
        '''Lấy dữ liệu từ cảm biến'''
        # tạo các biến chứa địa chỉ của các nodeId
        nodeId_temperature = "ns=3;i=16844288"
        nodeId_accum_flow = "ns=3;i=16843776"
        nodeId_instant_flow = "ns=3;i=16844032"
        nodeId_pressure = "ns=3;i=16844544"
        nodeId_standby = "ns=3;i=16847104"
        nodeId_force_standby ="ns=3;i=16847360"
        nodeId_ITV_NC = "ns=3;i=16847616"
        nodeId_ITV_NO = "ns=3;i=16847872"
        # Tạo các đối tượng nodeId
        temp = client.get_node(nodeId_temperature)    
        acuum_flow = client.get_node(nodeId_accum_flow)  
        instant_flow = client.get_node(nodeId_instant_flow)       
        press = client.get_node(nodeId_pressure)
        stand_signal = client.get_node(nodeId_standby)
        itv = client.get_node(nodeId_ITV_NC)
        # Tạo file 'csv' để lưu lịch sử dữ liệu
        with open("python_datas.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(['Time','Temperature','Accumulation Flow','Instantaneous Flow','Pressure'])
        
        while True: # Tạo vòng lặp để cập nhật dữ liệu 1s một lần
           
            # Đọc các giá trị từ server
            standby = stand_signal.get_value()
            temperature = round(temp.get_value()*0.1,1)
            accumulation_flow = acuum_flow.get_value()*10
            instantaneous_flow = instant_flow.get_value()
            pressure = press.get_value()
            if standby == False:
                self.accumflow_operation.append(instantaneous_flow/60)
            else:
                self.accumflow_standby.append(instantaneous_flow/60)
                if instantaneous_flow != 0:
                    self.flow_saving.append(self.accumflow_operation[-1])
                else:
                    self.flow_saving.append(0)
           


            self.x_time.append(self.x_time[-1]+1)
            self.y_pressure.append(pressure)
            self.y_instantflow.append(instantaneous_flow)
            self.y_temp.append(temperature)
            self.y_accumflow.append(accumulation_flow)

            if len(self.x_time) > 50:
                self.x_time = self.x_time[1:]
                self.y_pressure = self.y_pressure[1:]
                self.y_instantflow = self.y_instantflow[1:]
                self.y_temp = self.y_temp[1:]
# hiển thị các giá trị lên LCD
            self.lcd_temp.display('{:.02f}'.format(temperature))
            self.lcd_pressure.display(pressure)
            self.lcd_instantflow.display(instantaneous_flow)
            self.lcd_accumflow.display(accumulation_flow)

            now = datetime.now().strftime("%H:%M:%S")   

            self.data_pressure.setData(self.x_time,self.y_pressure)
            self.data_instantflow.setData(self.x_time,self.y_instantflow)
            self.data_accumflow.setData(self.y_accumflow)
            self.data_temp.setData(self.x_time,self.y_temp)
 # Ghi giá trị vào file 'csv'
            row  = [now,temperature,accumulation_flow,instantaneous_flow,pressure]
            with open('python_datas.csv',"a") as f:
                writer = csv.writer(f)
                writer.writerow(row)
            time.sleep(1)
               
    def update_barchart(self):
        a = 0
        c = [0,0,0]

        for i in self.accumflow_operation:
                c[0] += i
            
        for j in self.accumflow_standby:
                c[1] += j
            
        for k in self.flow_saving:
                a += k
        if a - c[1] > 0:
            c[2] = (a - c[1])
        else:
            c[2] = 0
            
        b = [f'Operation: {round(c[0],2)} L',f'Standby: {round(c[1],2)} L',f'Saving: {round(c[2],2)} L']
        x_axis = list(range(1,len(b)+1))
        ticks = []
        for i, item in enumerate(b):
            ticks.append((x_axis[i], item))
        ticks = [ticks]
        bargraph = pg.BarGraphItem(x = x_axis, height = c, width = 0.5, brush = 'green')
        self.graphicsView_compare.addItem(bargraph)
        ax = self.graphicsView_compare.getAxis('bottom')
        ax.setTicks(ticks)
    def disconnect_opc_server(self): # Ngắt kết nối khỏi server
        try:
            client.disconnect()
            self.lb_status.setText("Status: Disconnect")
        except:
            self.messege_box_information()
    

    def operation_mode(self):
        nodeId_standby = "ns=3;i=16847104"
        nodeId_force_standby ="ns=3;i=16847360"
        nodeId_ITV_NC = "ns=3;i=16847616"
        nodeId_ITV_NO = "ns=3;i=16847872"
        standby = client.get_node(nodeId_standby)
        force_standby = client.get_node(nodeId_force_standby)
        ITV_NO = client.get_node(nodeId_ITV_NO)
        ITV_NC = client.get_node(nodeId_ITV_NC)
        signal = self.value_to_datavalue(False)
        signal_ITV = self.value_to_datavalue(True)
        standby.set_data_value(signal)
        force_standby.set_data_value(signal)
        ITV_NC.set_data_value(signal_ITV)
        ITV_NO.set_data_value(signal_ITV)
        
        

    def value_to_datavalue(self,val, varianttype=None):
        """
        convert anything to a DataValue using varianttype
        """
        datavalue = None
        if isinstance(val, ua.DataValue):
            datavalue = val
        elif isinstance(val, ua.Variant):
            datavalue = ua.DataValue(val)
            #datavalue.SourceTimestamp = datetime.datetime.utcnow()
            datavalue.StatusCode = None
        else:
            datavalue = ua.DataValue(ua.Variant(val, varianttype))
            #datavalue.SourceTimestamp = datetime.datetime.utcnow()
            datavalue.StatusCode = None
        return datavalue
    

    def standby_mode(self):
        nodeId_ITV_NC = "ns=3;i=16847616"
        nodeId_standby = "ns=3;i=16847104"
        ITV_NC = client.get_node(nodeId_ITV_NC)
        standby = client.get_node(nodeId_standby)
        signal = self.value_to_datavalue(True)
        standby.set_data_value(signal)
        ITV_NC.set_data_value(signal)
    def isolation_mode(self):
        nodeId_ITV_NC = "ns=3;i=16847616"
        nodeId_ITV_NO = "ns=3;i=16847872"
        ITV_NO = client.get_node(nodeId_ITV_NO)
        ITV_NC = client.get_node(nodeId_ITV_NC)
        signal_ITV = self.value_to_datavalue(False)
        ITV_NC.set_data_value(signal_ITV)
        ITV_NO.set_data_value(signal_ITV)

    def messege_box_warning(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Warning")
        msg.setText("Check again URL Server or username and password !")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()
    def messege_box_information(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Information")
        msg.setText("Disconnected to server !")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()

            
    def remeber_information(self):
        # lưu thông tin người dùng
        with open("information.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(["Url","Username","Password"])
        if self.cb_remember.isChecked():
            row  = [self.le_url.text(),self.le_username.text(),self.le_password.text()]
            with open('information.csv',"a") as f:
                writer = csv.writer(f)
                writer.writerow(row)

    def get_info(self):
        # lấy thông tin người dùng
        data = pd.read_csv('information.csv')
        a = data["Url"]
        b = data["Username"]
        c = data["Password"]
        self.le_url.setText(a[0])
        self.le_username.setText(b[0])
        self.le_password.setText(c[0])
    def link_slot(self):
        # Tạo một luồng để xử lý tín hiệu
        try:
            worker = Worker(self.get_data)
            self.threadpool.start(worker)
        except:
            pass
        
           

if __name__ == '__main__':
    window  = QApplication(sys.argv)
    app = MainWindow()
    app.show()
    window.exec_()