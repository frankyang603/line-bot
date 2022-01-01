import urllib.request as req
def func(url):
    request=req.Request(url,headers={
        "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    #path = "output.txt"
    #f= open(path,"w",encoding="UTF-8")
    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("div",class_="table_container", id="div_roster")
    titles=root.tbody
    back="warrior player in 2021-22"+"\n"
    for tr in titles.children:
        if isinstance(tr, bs4.element.Tag):
            u = tr.find_all("td")
            back+=u[0].getText()
            print(u[0].getText())
            #print(u[0].a["href"])
            funcin("https://www.basketball-reference.com"+u[0].a["href"])
    account=0
    send_text_message(reply_token,back)
    return account

def funcin(url):
    request=req.Request(url,headers={
        "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("div",class_="table_container current" ,id="div_per_game")
    titles=root.tr
    for tr in titles:
        if isinstance(tr, bs4.element.Tag):
            back+=tr.getText()+" "
            print(tr.getText(),end=" ")
    print(end="\n")
    titles=root.tbody
    for tr in titles.children:
        if isinstance(tr, bs4.element.Tag):
            u = tr.find("th")
            back+=u.getText()+" "
            print(u.getText(),end=" ")
            u = tr.find_all("td")
            for i in range(0,29):
                print(u[i].getText(),end=" ")
            back+="\n"
            print(end="\n")
    account=0
    return account

#URL="https://www.basketball-reference.com/teams/GSW/2022.html"
#a=func(URL)