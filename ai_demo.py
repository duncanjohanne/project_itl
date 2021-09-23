import pandas as pd
import streamlit as st
import pickle
from main import calculate_delays

data = pd.read_csv("data.csv")
df = pd.DataFrame(data)
model = pickle.load(open('model.pkl', 'rb'))

st.title('Prediction of which end of a T-junction is booned based on traffic data collected')
hour_predict = st.text_input("Hour of Day 24hr(0-23)")
st.button('Predict')


if hour_predict:
    #defining a ratio of calculating delays from data
    filtered_per_hour = df.query("hour == "+str(hour_predict)+"")
    averageAB = int(filtered_per_hour['endABdelay'].mean())
    averageC = int(filtered_per_hour['endCdelay'].mean())
    countAB = int(filtered_per_hour['endAB'].mean())
    countC = int(filtered_per_hour['endC'].mean())

    vals = [hour_predict, countC, countAB, averageC, averageAB]
    pred_df = pd.DataFrame([vals], columns=['hour', 'endC', 'endAB', 'endCdelay', 'endABdelay'])

    prediction = model.predict(pred_df)
    st.write(''+str(prediction)+'')

    if prediction == 1:
        st.write('Neutral - Delays Equal')
        st.write('DelayC : '+str(10))
        st.write('DelayAB : '+str(10))
    if prediction == 0:
        cd = averageC + 10
        st.write('Preffered - EndC')
        st.write('DelayC : '+str(cd))
        st.write('DelayAB : '+str(averageAB))
    if prediction == 2:
        cd = averageAB + 10
        st.write('Preffered - EndAB')
        st.write('DelayAB : '+str(cd))
        st.write('DelayC : '+str(averageC))


    # for i in endCdelay:
    #     ctemp = 
    # print(averageC)




