import matplotlib.pyplot as plt
import threading
from kafka import KafkaConsumer

global aktTime
aktTime = 0

consumer = KafkaConsumer(bootstrap_servers ="localhost:9092")
consumer.subscribe(["Senseering-replicated"])

messageTime = []
messageLight = []
messageTemp = []
messagePressure = []
messageHumidity = []
messageXA = []
messageYA = []
messageZA = []
messageXG = []
messageYG = []
messageZG = []
messageXM = []
messageYM = []
messageZM = []
plotTime = []
plotLight = []
plotTemp = []
plotPressure = []
plotHumidity = []
plotXA = []
plotYA = []
plotZA = []
plotXG = []
plotYG = []
plotZG = []
plotXM = []
plotYM = []
plotZM = []


# This just simulates reading from a socket.
def data_listener():
    for message in consumer:
        daten = str(message.value).split("\\n")
        if(len(messageTime)==0):
            aktTime = int(daten[1].split(" ")[1])
        help = (aktTime == int(daten[1].split(" ")[1]))
        if  (int(daten[1].split(" ")[1]) != aktTime)and len(messageTime) > 0:
            anzElemente = messageTime.count(int(aktTime))
            plotTime.append(int(aktTime))
            summe = sum(messageLight[len(messageLight) - anzElemente:]) / float(anzElemente)
            plotLight.append(summe)
            summe = sum(messageTemp[len(messageTemp) - anzElemente:]) / float(anzElemente)
            plotTemp.append(summe)
            summe = sum(messagePressure[len(messagePressure) - anzElemente:]) / float(anzElemente)
            plotPressure.append(summe)
            summe = sum(messageHumidity[len(messageHumidity) - anzElemente:]) / float(anzElemente)
            plotHumidity.append(summe)
            summe = sum(messageXA[len(messageXA) - anzElemente:]) / float(anzElemente)
            plotXA.append(summe)
            summe = sum(messageYA[len(messageYA) - anzElemente:]) / float(anzElemente)
            plotYA.append(summe)
            summe = sum(messageZA[len(messageZA) - anzElemente:]) / float(anzElemente)
            plotZA.append(summe)
            summe = sum(messageXG[len(messageXG) - anzElemente:]) / float(anzElemente)
            plotXG.append(summe)
            summe = sum(messageYG[len(messageYG) - anzElemente:]) / float(anzElemente)
            plotYG.append(summe)
            summe = sum(messageZG[len(messageZG) - anzElemente:]) / float(anzElemente)
            plotZG.append(summe)
            summe = sum(messageXM[len(messageXM) - anzElemente:]) / float(anzElemente)
            plotXM.append(summe)
            summe = sum(messageYM[len(messageYM) - anzElemente:]) / float(anzElemente)
            plotYM.append(summe)
            summe = sum(messageZM[len(messageZM) - anzElemente:]) / float(anzElemente)
            plotZM.append(summe)
            aktTime = int(daten[1].split(" ")[1])
        messageTime.append(int(daten[1].split(" ")[1]))
        messageLight.append(int(daten[15].split(" ")[3]))
        messageTemp.append(int(daten[16].split(" ")[3]))
        messagePressure.append(int(daten[17].split(" ")[3]))
        messageHumidity.append(int(daten[18].split(" ")[3]))
        messageXA.append(int(daten[4].strip().split(' ')[2]))
        messageYA.append(int(daten[5].strip().split(' ')[2]))
        messageZA.append(int(daten[6].strip().split(' ')[2]))
        messageXG.append(int(daten[8].strip().split(' ')[2]))
        messageYG.append(int(daten[9].strip().split(' ')[2]))
        messageZG.append(int(daten[10].strip().split(' ')[2]))
        messageXM.append(int(daten[12].strip().split(' ')[2]))
        messageYM.append(int(daten[13].strip().split(' ')[2]))
        messageZM.append(int(daten[14].strip().split(' ')[2]))


        if (len(messageTime)>700):
            messageTime.pop(0)
            messageLight.pop(0)
            messageTemp.pop(0)
            messagePressure.pop(0)
            messageHumidity.pop(0)
        if(len(plotTime)>700):
            plotTime.pop(0)
            plotLight.pop(0)
            plotTemp.pop(0)
            plotPressure.pop(0)
            plotHumidity.pop(0)



if __name__ == '__main__':
    thread = threading.Thread(target=data_listener)
    thread.daemon = True
    thread.start()

    #
    # initialize figure
    labelPlot =False
    plt.rcParams['toolbar']='None'
    fig, axes = plt.subplots(2,2)
    fig2,axes2 = plt.subplots(2,2)
    fig3,axes3 = plt.subplots(1,1)
    fig4,axes4 = plt.subplots(2,2)
    fig5,axes5 = plt.subplots(1,1)
    fig6, axes6 = plt.subplots(2, 2)
    fig7, axes7 = plt.subplots(1, 1)
    fig2.delaxes(axes2[1,1])
    fig4.delaxes(axes4[1, 1])
    fig6.delaxes(axes6[1, 1])
    fig.canvas.set_window_title('Environment')
    fig2.canvas.set_window_title('Vibration')
    fig3.canvas.set_window_title('Vibration-X,Y,Z')
    fig4.canvas.set_window_title('Gyroscope')
    fig5.canvas.set_window_title('Gyroscope-X,Y,Z')
    fig6.canvas.set_window_title('Magnetic Field')
    fig7.canvas.set_window_title('Magnetic Field-X,Y,Z')
    plt.ion()
    plt.show()
    while True:
        if(len(plotTime)>0):
            plt.pause(1)
            #Titel
            axes[0,0].set_title('Humidity')
            axes[0, 1].set_title('Temperature')
            axes[1, 0].set_title('Pressure')
            axes[1, 1].set_title('Light')
            axes2[0, 0].set_title('X-Acceleration')
            axes2[0, 1].set_title('Y-Acceleration')
            axes2[1, 0].set_title('Z-Acceleration')
            axes3.set_title('Acceleration')
            axes4[0, 0].set_title('X-Gyroscope')
            axes4[0, 1].set_title('Y-Gyroscope')
            axes4[1, 0].set_title('Z-Gyroscope')
            axes5.set_title('Gyroscope')
            axes6[0, 0].set_title('X-Magnetic Field')
            axes6[0, 1].set_title('Y-Magnetic Field')
            axes6[1, 0].set_title('Z-Magnetic Field')
            axes7.set_title('Magnetic Field')
            #x-Label
            for i in range(2):
                for j in range(2):
                    axes[i, j].set_xlabel('Time[s]')
                    if i == 0 or j == 0:
                        axes2[i, j].set_xlabel('Time[s]')
                        axes4[i, j].set_xlabel('Time[s]')
                        axes6[i, j].set_xlabel('Time[s]')
            axes3.set_xlabel('Time[s]')
            axes5.set_xlabel('Time[s]')
            axes7.set_xlabel('Time[s]')
            #y-Label
            axes[0, 0].set_ylabel('%rh')
            axes[0, 1].set_ylabel('mCelsius')
            axes[1, 0].set_ylabel('Pascal')
            axes[1, 1].set_ylabel('mLux')
            axes2[0, 0].set_ylabel('mG')
            axes2[0, 1].set_ylabel('mG')
            axes2[1, 0].set_ylabel('mG')
            axes3.set_ylabel('mG')
            axes4[0, 0].set_ylabel('mdeg/s')
            axes4[0, 1].set_ylabel('mdeg/s')
            axes4[1, 0].set_ylabel('mdeg/s')
            axes5.set_ylabel('mdeg/s')
            axes6[0, 0].set_ylabel('uT')
            axes6[0, 1].set_ylabel('uT')
            axes6[1, 0].set_ylabel('uT')
            axes3.set_ylabel('uT')
            #grid and xlim
            for i in range(2):
                for j in range(2):
                    axes[i,j].grid(b=True)
                    axes[i,j].set_xlim(plotTime[0], plotTime[len(plotTime) - 1])
                    if i == 0 or j == 0:
                        axes2[i,j].grid(b=True)
                        axes2[i, j].set_xlim(plotTime[0], plotTime[len(plotTime) - 1])
                        axes4[i, j].grid(b=True)
                        axes4[i, j].set_xlim(plotTime[0], plotTime[len(plotTime) - 1])
                        axes6[i, j].grid(b=True)
                        axes6[i, j].set_xlim(plotTime[0], plotTime[len(plotTime) - 1])
            axes3.grid(b=True)
            axes5.grid(b=True)
            axes7.grid(b=True)
            axes3.set_xlim(plotTime[0], plotTime[len(plotTime) - 1])
            axes5.set_xlim(plotTime[0], plotTime[len(plotTime) - 1])
            axes7.set_xlim(plotTime[0], plotTime[len(plotTime) - 1])
            #ylim
            axes[0,0].set_ylim(min(plotHumidity)-2, max(plotHumidity)+2)
            axes[0, 1].set_ylim(min(plotTemp) - 200, max(plotTemp) + 200)
            axes[1, 0].set_ylim(min(plotPressure) - 200, max(plotPressure) + 200)
            axes[1, 1].set_ylim(min(plotLight) - 1000, max(plotLight) + 1000)
            axes2[0, 0].set_ylim(min(plotXA) - 50, max(plotXA) + 50)
            axes2[0, 1].set_ylim(min(plotYA) - 50, max(plotYA) + 50)
            axes2[1, 0].set_ylim(min(plotZA) - 50, max(plotZA) + 50)
            axes3.set_ylim(min([min(plotXA),min(plotYA),min(plotZA)]) - 50, max([max(plotXA),max(plotYA),max(plotZA)]) + 50)
            axes4[0, 0].set_ylim(min(plotXG) - 50, max(plotXG) + 50)
            axes4[0, 1].set_ylim(min(plotYG) - 50, max(plotYG) + 50)
            axes4[1, 0].set_ylim(min(plotZG) - 50, max(plotZG) + 50)
            axes5.set_ylim(min([min(plotXG), min(plotYG), min(plotZG)]) - 50,
                           max([max(plotXG), max(plotYG), max(plotZG)]) + 50)
            axes6[0, 0].set_ylim(min(plotXM) - 50, max(plotXM) + 50)
            axes6[0, 1].set_ylim(min(plotYM) - 50, max(plotYM) + 50)
            axes6[1, 0].set_ylim(min(plotZM) - 50, max(plotZM) + 50)
            axes7.set_ylim(min([min(plotXM), min(plotYM), min(plotZM)]) - 50,
                           max([max(plotXM), max(plotYM), max(plotZM)]) + 50)
            axes[0, 0].plot(plotTime, plotHumidity, color="#006db6", linewidth=2.0)
            axes[0, 1].plot(plotTime, plotTemp, color="#ff9900", linewidth=2.0)
            axes[1, 0].plot(plotTime, plotPressure, color="#ff0000", linewidth=2.0)
            axes[1, 1].plot(plotTime, plotLight, color="#000000", linewidth=2.0)
            axes2[0, 0].plot(plotTime, plotXA, color="#006db6", linewidth=2.0)
            axes2[0, 1].plot(plotTime, plotYA, color="#ff9900", linewidth=2.0)
            axes2[1, 0].plot(plotTime, plotZA, color="#ff0000", linewidth=2.0)
            axes3.plot(plotTime, plotXA, color="#006db6", linewidth=2.0,label='X')
            axes3.plot(plotTime, plotYA, color="#ff9900", linewidth=2.0,label='Y')
            axes3.plot(plotTime, plotZA, color="#ff0000", linewidth=2.0,label='Z')
            axes4[0, 0].plot(plotTime, plotXG, color="#006db6", linewidth=2.0)
            axes4[0, 1].plot(plotTime, plotYG, color="#ff9900", linewidth=2.0)
            axes4[1, 0].plot(plotTime, plotZG, color="#ff0000", linewidth=2.0)
            axes5.plot(plotTime, plotXG, color="#006db6", linewidth=2.0, label='X')
            axes5.plot(plotTime, plotYG, color="#ff9900", linewidth=2.0, label='Y')
            axes5.plot(plotTime, plotZG, color="#ff0000", linewidth=2.0, label='Z')
            axes6[0, 0].plot(plotTime, plotXM, color="#006db6", linewidth=2.0)
            axes6[0, 1].plot(plotTime, plotYM, color="#ff9900", linewidth=2.0)
            axes6[1, 0].plot(plotTime, plotZM, color="#ff0000", linewidth=2.0)
            axes7.plot(plotTime, plotXM, color="#006db6", linewidth=2.0, label='X')
            axes7.plot(plotTime, plotYM, color="#ff9900", linewidth=2.0, label='Y')
            axes7.plot(plotTime, plotZM, color="#ff0000", linewidth=2.0, label='Z')
            if(labelPlot==False):
                labelPlot = True
                axes3.legend(loc=0)
                axes5.legend(loc=0)
                axes7.legend(loc=0)