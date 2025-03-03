import streamlit as st

page = st.sidebar.radio("鸟戾天时：",["首页","信息","下载","我的","支持我们"])


def page1():
    st.balloons()
    #文字
    st.image("there_is_whenFly.jpg")
    st.image("welcome.jpg")
    st.image("Apics/招聘.png")
    #st.audio()
    #st.video()

def page2():
    st.image("aboutUs.jpg")
    tab1,tab2,tab3 = st.tabs(["程序逻辑","联系我们","制作者"])
    with tab1:
        st.write("鸟戾天时的程序毫无逻辑，请不要尝试寻找代码的逻辑。")
    with tab2:
        st.write("你把我开了你才可以联系我哦")
    with tab3:
        st.image("Apics/maker/GaoA1.png")
        st.write("（↑美丽的制作者↑）")
        st.write("制作者：拐到缺德和巧克力饼")

def page3():
    st.image("Apics/JerryZhang/chaosBird.png")
    with open("Apics/JerryZhang/chaosBird.png", "rb") as file:
        btn = st.download_button(
            label="点击下载十分精美的张少博美图-我阐述你的梦",
            data=file,
            file_name="Apics/JerryZhang/chaosBird.png",
            mime="image/png"
        )
    st.image("Apics/JerryZhang/coolBird.png")
    with open("Apics/JerryZhang/coolBird.png", "rb") as file:
        btn = st.download_button(
            label="点击下载十分精美的张少博美图-酷炫2代鸟神",
            data=file,
            file_name="Apics/JerryZhang/coolBird.png",
            mime="image/png"
        )
    st.image("Apics/JerryZhang/cuteBird.png")
    with open("Apics/JerryZhang/cuteBird.png", "rb") as file:
        btn = st.download_button(
            label="点击下载十分精美的张少博美图-可爱小鸟",
            data=file,
            file_name="Apics/JerryZhang/cuteBird.png",
            mime="image/png"
        )

def page4():
    st.write("你在这里一无所有")

def page5():
    st.write("本来想在这里放一个付款码的，但是太缺德了，没放:(")


if page == '首页':
    page1()
elif page == '信息':
    page2()
elif page == '下载':
    page3()
elif page == '我的':
    page4()
elif page == '支持我们':
    page5()