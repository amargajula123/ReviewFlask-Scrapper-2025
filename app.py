from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import os
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq # uReq is the alias or object / variable of urlopen
import pandas as pd

app = Flask(__name__)

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/review',methods=['POST','GET']) # route to show the review comments in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            searchString = request.form['content'].replace(" ","")
            print("request.form['content'] :",request.form['content'])
            flipkart_url = "https://www.flipkart.com/search?q=" + searchString
            uClient = uReq(flipkart_url)
            flipkartPage = uClient.read()
            uClient.close()
            flipkart_html = bs(flipkartPage, "html.parser")
            bigboxes = flipkart_html.findAll("div", {"class": "cPHDOP col-12-12"})
            del bigboxes[0:3]
            box = bigboxes[0]
            productLink = "https://www.flipkart.com" + box.div.div.div.a['href']
            prodRes = requests.get(productLink)
            prodRes.encoding='utf-8'
            prod_html = bs(prodRes.text, "html.parser")
            print(prod_html)
            commentboxes = prod_html.find_all('div', {'class': "RcXBOT"})

            # filename = searchString + ".csv"
            # fw = open(filename, "w")
            # headers = "Product, Customer Name, Rating, Heading, Comment \n"
            # fw.write(headers)
            reviews = []
            for commentbox in commentboxes:
                try:
                    #name.encode(encoding='utf-8')
                    name = commentbox.div.div.find_all('p', {'class': "_2NsDsF AwS1CA"})[0].text
                    #name = commentboxes[i].div.div.find_all('p', {'class': '_2NsDsF AwS1CA'})[0].text

                except:
                    name = 'No Name'

                try:
                    #rating.encode(encoding='utf-8')
                    rating = commentbox.div.div.div.div.text


                except:
                    rating = 'No Rating'

                try:
                    #commentHead.encode(encoding='utf-8')
                    commentHead = commentbox.div.div.div.p.text

                except:
                    commentHead = 'No Comment Heading'
                try:
                    #comtag = commentbox.div.div.find_all('div', {'class': ''})
                    comtag = commentbox.div.div.find_all('div', {'class': ''})
                            #commentboxes[i].find_all('div', {'class': ''})
                    #custComment.encode(encoding='utf-8')
                    custComment = comtag[0].div.text
                except Exception as e:
                    print("Exception while creating dictionary: ",e)

                mydict = {"Product": searchString, "Name": name, "Rating": rating, "CommentHead": commentHead,
                          "Comment": custComment}
                reviews.append(mydict)
                df = pd.DataFrame(reviews)
                df.to_csv(f"{searchString}"+".csv",index=False)
            return render_template('results.html', reviews=reviews[0:(len(reviews)-1)])
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    # return render_template('results.html')

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)

    # port = int(os.environ.get("PORT", 5000))  # Get port from Heroku, default to 5000 locally
    # app.run(host="0.0.0.0", port=port, debug=True)




    #app.run(host='127.0.0.1', port=80, debug=True)
	#app.run(debug=True)

    # for i in range(len(commentboxes) - 1):
          # comment head
    #     print(commentboxes[i].find_all('p', {'class': 'z9E0IG'})[0].text)
          # customer name
    #     print(commentboxes[i].find_all('p', {'class': '_2NsDsF AwS1CA'})[0].text)
          # rating of customer
    #     # print(commentboxes[i].div.div.div.div.text)
    #     print(commentboxes[i].find_all('div', {'class': 'XQDdHH Ga3i8K'})[0].text)
          # full comment of customer
    #     print(commentboxes[i].find_all('div', {'class': 'ZmyHeo'})[0].text)
    #     custag = commentboxes[i].find_all('div',{'class': ''})  # ZmyHeo if you use class name READ MORE string will be shown
        # print("cmmnt2 :", custag[0].div.text)                  # if not use this class name "ZmyHeo" it only show total comment string
        # print('\n')