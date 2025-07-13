'''我的主页'''
import streamlit as st
from PIL import Image
page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区', "神秘问答"])

def page_1():
    '''我的兴趣推荐'''
    st.balloons()
    st.write("666直接给我坐下！！！")
    with open('叱咤风云.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    
    st.image("权威.jpg")

    st.write('神秘选项')
    st.write('----')
    level = st.radio(
        '感觉我怎么样',
        ['牛逼666', '有实力', '开桂了'],
        captions=['立加七大玉牛逼666', '立加七大玉泰有实力辣', '立加七大玉盖世无双']
    )
    
def page_2():
    '''我的图片处理工具'''
    st.write('谁敢笑')
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    tab1,tab2,tab3,tab4=st.tabs(["原图","换色1","换色2","换色3"])
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        #st.image(img)
        #st.image(img_change(img, 0, 2, 1))
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 2, 1, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2))


def page_3():
    '''我的智能词典'''
    st.write("智能词典")
    #从本地读取并存储
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    #进行分割
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    #导入字典
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
        with open('check_out_times.txt', 'r', encoding='utf-8') as f:
            times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    #创建输入框
    word = st.text_input('请输入要查询的单词（如apple）')
    #显示
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message=message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])
        
def page_4():
    st.snow()
    st.write('我的留言区')
    # 从文件中加载内容，并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '无语新':
            with st.chat_message('🌞'):
                st.write(i[1],':',i[2])
        elif i[1] == '胃汁':
            with st.chat_message('🍥'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是……', ['无语新', '胃汁'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)

    st.write('----')
    st.write('炒鸡传送门')
    go = st.selectbox('你的支持是我最大的动力，去支持一下up吧！', ['我的贴吧', '我的bilibili'])
    if go == '我的贴吧':
        st.link_button('帮我盖楼', 'https://www.baidu.com/')
    elif go == '我的bilibili':
        st.link_button('帮我一键三连', 'https://www.bilibili.com/')

def page_5():
    st.write('----')
    st.write('是否承认立加七大玉盖世无双')
    cb1 = st.checkbox('是')
    cb2 = st.checkbox('否')
    cb3 = st.checkbox('必须承认')
    cb4 = st.checkbox('立加七大玉盖世无双')
    l = [cb2]
    if st.button('确认答案'):
        if True in l:
            st.write('666居然不承认给我重选！！！')
        else:
            st.write('立加七牛逼无敌666')



    
            
def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img
if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == '神秘问答':
    page_5()