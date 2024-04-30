import streamlit as st 
import time
import datetime
import playsound

st.markdown("# Timer App")
st.markdown("---")

t = st.time_input("Set an alarm for",value=None)
st.write("Alarm is set for",t)

def get_time():
    global t
    if t!= None:
        def rerun():
            st.rerun()
            
        btn = st.button("Stop",type="primary",on_click=rerun)
        str_time = str(t)
        lst = str_time.split(":")
        hours = int(lst[0])
        minutes = int(lst[1])
        seconds = 0
        minutes+= hours*60
        seconds+= minutes*60
        bar = st.progress(0)
        step_val = int(seconds)//100
        val = 0
        
        for i in range(seconds):
            val+=step_val
            time.sleep(1)
            #bar.progress(val)
        else:
            is_completed = True
        
        if is_completed:
            playsound.playsound('alarm.mp3',True)
        

        
    else:
        st.error("Time cannot be set to None")
    

st.button("Start",type="primary",on_click=get_time)