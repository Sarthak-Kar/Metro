from dearpygui.core import*
from dearpygui.simple import*
import pyfiglet
import html2text
import custom_google
import textwrap
from bs4 import BeautifulSoup

page=0
list_ids=[]
oldmessage=" "
msg1="Message 1"   
msg2="Message 2"
msg3="Message 3"
msg4="Message 4"
msg5="Message 5"
msg6="Message 6"
msg7="Message 7"
msg8="Message 8"
msg9="Message 9"
msg10="Message 10"
oldsam1="Message 1"
oldsam2="Message 2"
oldsam3="Message 3"
oldsam4="Message 4"
oldsam5="Message 5"
oldsam6="Message 6"
oldsam7="Message 7"
oldsam8="Message 8"
oldsam9="Message 9"
oldsam10="Message 10"
sender="from"
service=custom_google.main()
files=[]

def add_Button():
    global oldsam1
    global oldsam2
    global oldsam3
    global oldsam4
    global oldsam5
    global oldsam6
    global oldsam7
    global oldsam8
    global oldsam9
    global oldsam10
    global msg1
    global msg2
    global msg3
    global msg4
    global msg5
    global msg6
    global msg7
    global msg8
    global msg9
    global msg10
    global sender
    msg2=str(2+page*10)+"  "+custom_google.get_message_details(service, 'me', list_ids[1+page*10])[sender][:17]+"....    "+custom_google.get_message_details(service, 'me', list_ids[1+page*10])["subject"][:46]+"                                                           "
    delete_item(oldsam2)
    add_button(msg2, parent="Metro",callback=view_message, callback_data=list_ids[1+page*10])
    
    msg3=str(3+page*10)+"  "+custom_google.get_message_details(service, 'me', list_ids[2+page*10])[sender][:17]+"....    "+custom_google.get_message_details(service, 'me', list_ids[2+page*10])["subject"][:46]+"                                                           "
    delete_item(oldsam3)
    add_button(msg3, parent="Metro",callback=view_message, callback_data=list_ids[2+page*10])
    
    msg4=str(4+page*10)+"  "+custom_google.get_message_details(service, 'me', list_ids[3+page*10])[sender][:17]+"....    "+custom_google.get_message_details(service, 'me', list_ids[3+page*10])["subject"][:46]+"                                                           "
    delete_item(oldsam4)
    add_button(msg4, parent="Metro",callback=view_message, callback_data=list_ids[3+page*10])
    
    msg5=str(5+page*10)+"  "+custom_google.get_message_details(service, 'me', list_ids[4+page*10])[sender][:17]+"....    "+custom_google.get_message_details(service, 'me', list_ids[4+page*10])["subject"][:46]+"                                                           "
    delete_item(oldsam5)
    add_button(msg5, parent="Metro",callback=view_message, callback_data=list_ids[4+page*10])

    msg6=str(6+page*10)+"  "+custom_google.get_message_details(service, 'me', list_ids[5+page*10])[sender][:17]+"....    "+custom_google.get_message_details(service, 'me', list_ids[5+page*10])["subject"][:46]+"                                                           "
    delete_item(oldsam6)
    add_button(msg6, parent="Metro",callback=view_message, callback_data=list_ids[5+page*10])
    
    msg7=str(7+page*10)+"  "+custom_google.get_message_details(service, 'me', list_ids[6+page*10])[sender][:17]+"....    "+custom_google.get_message_details(service, 'me', list_ids[6+page*10])["subject"][:46]+"                                                           "
    delete_item(oldsam7)
    add_button(msg7, parent="Metro",callback=view_message, callback_data=list_ids[6+page*10])
    
    msg8=str(8+page*10)+"  "+custom_google.get_message_details(service, 'me', list_ids[7+page*10])[sender][:17]+"....    "+custom_google.get_message_details(service, 'me', list_ids[7+page*10])["subject"][:46]+"                                                           "
    delete_item(oldsam8)
    add_button(msg8, parent="Metro",callback=view_message, callback_data=list_ids[7+page*10])
    
    msg9=str(9+page*10)+"  "+custom_google.get_message_details(service, 'me', list_ids[8+page*10])[sender][:17]+"....    "+custom_google.get_message_details(service, 'me', list_ids[8+page*10])["subject"][:46]+"                                                           "
    delete_item(oldsam9)
    add_button(msg9, parent="Metro",callback=view_message, callback_data=list_ids[8+page*10])
    
    msg10=str(10+page*10)+"  "+custom_google.get_message_details(service, 'me', list_ids[9+page*10])[sender][:17]+"....    "+custom_google.get_message_details(service, 'me', list_ids[9+page*10])["subject"][:46]+"                                                           "
    delete_item(oldsam10)
    add_button(msg10, parent="Metro",callback=view_message, callback_data=list_ids[9+page*10])

def inbox():
    global page
    global sender
    sender="from"
    page=0
    file=open("inbox.txt",'w')
    file.seek(0)
    file.truncate()
    global list_ids
    list_ids=custom_google.get_inbox(service)
    if(len(list_ids)<100):
        for i in range(0, 100-len(list_ids), 1):
            list_ids.append('0')
    s1=','.join(list_ids)
    file.write(s1)
    file.close()
    file=open("inbox.txt",'r')
    for data in file:
        list_ids=data.split(",")
    file.close()
    global oldsam1
    global oldsam2
    global oldsam3
    global oldsam4
    global oldsam5
    global oldsam6
    global oldsam7
    global oldsam8
    global oldsam9
    global oldsam10
    global msg1
    global msg2
    global msg3
    global msg4
    global msg5
    global msg6
    global msg7
    global msg8
    global msg9
    global msg10
    oldsam1=msg1
    oldsam2=msg2
    oldsam3=msg3
    oldsam4=msg4
    oldsam5=msg5
    oldsam6=msg6
    oldsam7=msg7
    oldsam8=msg8
    oldsam9=msg9
    oldsam10=msg10
    msg1=str(1+page*10)+"  "+custom_google.get_message_details(service, 'me', list_ids[0])[sender][:17]+"....    "+custom_google.get_message_details(service, 'me', list_ids[0])["subject"][:46]+"                                                           "
    if(oldsam1==msg1):
        return None
    delete_item(oldsam1)
    add_button(msg1, parent="Metro", callback=view_message, callback_data=list_ids[0])
    add_Button()
    
    

def press():
    global page
    print(page)

def page_decrease():
    global page
    global sender
    if(page>0):
        page-=1
    else:
        return None
    global list_ids
    global oldsam1
    global oldsam2
    global oldsam3
    global oldsam4
    global oldsam5
    global oldsam6
    global oldsam7
    global oldsam8
    global oldsam9
    global oldsam10
    global msg1
    global msg2
    global msg3
    global msg4
    global msg5
    global msg6
    global msg7
    global msg8
    global msg9
    global msg10
    oldsam1=msg1
    oldsam2=msg2
    oldsam3=msg3
    oldsam4=msg4
    oldsam5=msg5
    oldsam6=msg6
    oldsam7=msg7
    oldsam8=msg8
    oldsam9=msg9
    oldsam10=msg10
    
    msg1=str(1+page*10)+"  "+custom_google.get_message_details(service, 'me', list_ids[0+page*10])[sender][:17]+"....    "+custom_google.get_message_details(service, 'me', list_ids[0+page*10])["subject"][:46]+"                                                           "
    if(oldsam1==msg1):
        return None
    delete_item(oldsam1)
    add_button(msg1, parent="Metro",callback=view_message, callback_data=list_ids[0+page*10])
    add_Button() 
   
def page_increase():
    global page
    global sender
    page+=1
    global list_ids
    global oldsam1
    global oldsam2
    global oldsam3
    global oldsam4
    global oldsam5
    global oldsam6
    global oldsam7
    global oldsam8
    global oldsam9
    global oldsam10
    global msg1
    global msg2
    global msg3
    global msg4
    global msg5
    global msg6
    global msg7
    global msg8
    global msg9
    global msg10
    oldsam1=msg1
    oldsam2=msg2
    oldsam3=msg3
    oldsam4=msg4
    oldsam5=msg5
    oldsam6=msg6
    oldsam7=msg7
    oldsam8=msg8
    oldsam9=msg9
    oldsam10=msg10
    msg1=str(1+page*10)+"  "+custom_google.get_message_details(service, 'me', list_ids[0+page*10])[sender][:17]+"....    "+custom_google.get_message_details(service, 'me', list_ids[0+page*10])["subject"][:46]+"                                                           "
    if(oldsam1==msg1):
        return None
    delete_item(oldsam1)
    add_button(msg1, parent="Metro",callback=view_message, callback_data=list_ids[0+page*10])
    add_Button()

def view_message(sender, data):
    returning=custom_google.message_details(service, data)
    text1=returning["date"]+"\n\n"+returning["from"]+"\n\n"+returning["subject"]+"\n\n\n"
    text=custom_google.get_message(service,'me', data)
    global oldmessage
    if(text==oldmessage):
        return None
    #wrapper = textwrap.TextWrapper(width=45)  
    #word_list = wrapper.wrap(text=text)
    #text='\n'.join(word_list)
    #try:
    #text=html2text.html2text(text)
    try:
        text=text1+text
    except:
        text=custom_google.exp(service, data)
        text=text1+text
        
    #except :
    #   text=text1+text
    #print(text)
    delete_item(oldmessage)
    add_text(text, parent="Details")
    
    oldmessage=text

def search_msg():
    input_value=get_value(".")
    global page
    global sender
    sender = "from"
    page=0
    file=open("inbox.txt",'w')
    file.seek(0)
    file.truncate()
    global list_ids
    list_ids=custom_google.search_message(service,'me',input_value)
    if(len(list_ids)==0):
        list_ids=[]
    if(len(list_ids)<100):
        for i in range(0, 100-len(list_ids), 1):
            list_ids.append('0')
    s1=','.join(list_ids)
    file.write(s1)
    file.close()
    file=open("inbox.txt",'r')
    for data in file:
        list_ids=data.split(",")
    file.close()
    global oldsam1
    global oldsam2
    global oldsam3
    global oldsam4
    global oldsam5
    global oldsam6
    global oldsam7
    global oldsam8
    global oldsam9
    global oldsam10
    global msg1
    global msg2
    global msg3
    global msg4
    global msg5
    global msg6
    global msg7
    global msg8
    global msg9
    global msg10
    oldsam1=msg1
    oldsam2=msg2
    oldsam3=msg3
    oldsam4=msg4
    oldsam5=msg5
    oldsam6=msg6
    oldsam7=msg7
    oldsam8=msg8
    oldsam9=msg9
    oldsam10=msg10
    msg1=str(1+page*10)+"  "+custom_google.get_message_details(service, 'me', list_ids[0+page*10])[sender][:17]+"....    "+custom_google.get_message_details(service, 'me', list_ids[0+page*10])["subject"][:46]+"                                                           "
    if(oldsam1==msg1):
        return None
    delete_item(oldsam1)
    add_button(msg1, parent="Metro",callback=view_message, callback_data=list_ids[0+page*10])
    add_Button()

def sent_items():
    global page
    global sender
    sender='to'
    page=0
    file=open("inbox.txt",'w')
    file.seek(0)
    file.truncate()
    global list_ids
    list_ids=custom_google.sent_mails(service,'me')
    if(len(list_ids)<100):
        for i in range(0, 100-len(list_ids), 1):
            list_ids.append('0')
    s1=','.join(list_ids)
    file.write(s1)
    file.close()
    file=open("inbox.txt",'r')
    for data in file:
        list_ids=data.split(",")
    file.close()
    global oldsam1
    global oldsam2
    global oldsam3
    global oldsam4
    global oldsam5
    global oldsam6
    global oldsam7
    global oldsam8
    global oldsam9
    global oldsam10
    global msg1
    global msg2
    global msg3
    global msg4
    global msg5
    global msg6
    global msg7
    global msg8
    global msg9
    global msg10
    oldsam1=msg1
    oldsam2=msg2
    oldsam3=msg3
    oldsam4=msg4
    oldsam5=msg5
    oldsam6=msg6
    oldsam7=msg7
    oldsam8=msg8
    oldsam9=msg9
    oldsam10=msg10
    msg1=str(1+page*10)+"  "+custom_google.get_message_details(service, 'me', list_ids[0])[sender][:17]+"....    "+custom_google.get_message_details(service, 'me', list_ids[0])["subject"][:46]+"                                                           "
    if(oldsam1==msg1):
        return None
    delete_item(oldsam1)
    add_button(msg1, parent="Metro", callback=view_message, callback_data=list_ids[0])
    add_Button()

def file_picker(sender, data):
    open_file_dialog(callback=apply_selected_file, extensions=".*,.py")

def apply_selected_file(sender, data):
    global files
    directory = data[0]
    file = data[1]
    set_value("directory", directory)
    set_value("file", file)
    set_value("file_path", f"{directory}\\{file}")
    files.append(data[0]+"\\"+data[1])

def send():
    global files
    destination=get_value("##to")
    subject=get_value("##sub")
    body=get_value("##body")
    custom_google.send_message(service, destination, subject, body, files)
    

set_main_window_size(1285, 720)
set_global_font_scale(1.25)
set_theme("Light")
set_style_window_padding(20,0)
#add_additional_font("CONSOLA.ttf")

#show_style_editor()

with window("Metro", width= 810, height=477):
    #print(pyfiglet.figlet_format("Metro"))
    set_window_pos("Metro", 0, 0)
    page=0
    add_text(pyfiglet.figlet_format("Metro"))
    add_spacing(count=2)
    add_button("Inbox", callback=inbox)
    add_same_line()
    add_button("<", callback=page_decrease)
    add_same_line()
    add_button(">", callback=page_increase)
    add_same_line()
    add_button("Sent items", callback=sent_items)
    add_same_line()
    add_dummy(width=240)
    add_same_line()
    add_input_text(".", width=187)
    add_same_line()
    add_button("Search", callback=search_msg)
    add_spacing(count=8)
    add_button(msg1, callback=press)
    add_button(msg2, callback=press)
    add_button(msg3, callback=press)
    add_button(msg4, callback=press)
    add_button(msg5, callback=press) 
    add_button(msg6, callback=press)   
    add_button(msg7, callback=press)   
    add_button(msg8, callback=press)
    add_button(msg9, callback=press)
    add_button(msg10, callback=press)   
    
with window("Details", width= 460, height=477):
    set_window_pos("Details", 810, 0)
    add_spacing(count=20)
    add_text(oldmessage, wrap=50)

with window("Kompose", width=1270, height=203):
    set_window_pos("Kompose",0,477)
    add_spacing(count=2)
    add_text("To:")
    add_same_line()
    add_dummy(width=10)
    add_same_line()
    add_same_line()
    add_input_text("##to", width=300)
    add_same_line()
    add_text("Subject:")
    add_same_line()
    add_input_text("##sub", width=595)
    add_same_line()
    add_button("Add Attachment", callback=file_picker)
    add_same_line()
    add_button("Send", callback=send)
    add_text("Body:")
    add_same_line()
    add_input_text("##body", multiline=True, width=1260)
    print("s")


start_dearpygui()
