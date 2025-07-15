from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import os
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq # uReq is the alias or object / variable of urlopen
import pandas as pd

<<<<<<< HEAD
=======
import sys
from exception import ReviewException
from logger import logging

# NOTE : for this project use ver_env is "ReviewFlask_env_3"

>>>>>>> fe0a16e ( Added exception , logger ,Procfile ,templates ,test)
app = Flask(__name__)

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
<<<<<<< HEAD
    return render_template("index.html")
=======
    return render_template("index.html")   #  render = ఇవ్వడం / అందించు
>>>>>>> fe0a16e ( Added exception , logger ,Procfile ,templates ,test)

@app.route('/review',methods=['POST','GET']) # route to show the review comments in a web UI
@cross_origin()
def index():
<<<<<<< HEAD
    if request.method == 'POST':
        try:
            searchString = request.form['content'].replace(" ","")
            print("request.form['content'] :",request.form['content'])
            flipkart_url = "https://www.flipkart.com/search?q=" + searchString
            uClient = uReq(flipkart_url)
=======
    logging.info(f"{'*'*10}Review_Flask-Scrapper-2025is started{'*'*10}")
    if request.method == 'POST':
        logging.info("yes requested methode is Post ")
        try:
            searchString = request.form['content'].replace(" ","")
            if not searchString:
                logging.info("Please enter a product name kindly...")
                return render_template("index.html", error="⚠️ Please enter a product name.")
            print(f"searchString = {searchString}")
            logging.info(f"user looking for : {searchString}")
            print("request.form['content'] = ",request.form['content'])
            flipkart_url = "https://www.flipkart.com/search?q=" + searchString
            logging.info(f"flipkart_url : [{flipkart_url}]")
            uClient = uReq(flipkart_url) # we are pinging the url here
>>>>>>> fe0a16e ( Added exception , logger ,Procfile ,templates ,test)
            flipkartPage = uClient.read()
            uClient.close()
            flipkart_html = bs(flipkartPage, "html.parser")
            bigboxes = flipkart_html.findAll("div", {"class": "cPHDOP col-12-12"})
<<<<<<< HEAD
            del bigboxes[0:3]
=======
            if len(bigboxes) > 3:
                del bigboxes[0:3]
                logging.info("deleted the 1st 3 boxes(list) of information")
            else:
                raise ReviewException("Not enough product boxes found",sys)
            # del bigboxes[0:3]  # why deleting frant 3 infor means there we wont find and "href"

>>>>>>> fe0a16e ( Added exception , logger ,Procfile ,templates ,test)
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
<<<<<<< HEAD
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
=======
            logging.info("extracting 'name','rating','commentHead','custComment' is started")
            for commentbox in commentboxes:
                # name = commentbox.find_all('p', {'class': "_2NsDsF AwS1CA"})[0].text
                try:
                    name_tag = commentbox.find('p', {'class': "_2NsDsF AwS1CA"})
                    name = name_tag.text.strip() if name_tag else "No Name"
                    if not name_tag:
                        pass
                except Exception as e:
                    name = "No Name"
                    raise ReviewException(e, sys) from e

                try:
                    rating_tag = commentbox.div.div.div.div
                    rating = rating_tag.text if rating_tag else "No Rating"
                    if not rating_tag:
                        raise Exception("Rating tag not found")
                except Exception as e:
                    rating = "No Rating"


                try:
                    comment_head_tag = commentbox.div.div.div.p
                    commentHead = comment_head_tag.text if comment_head_tag else "No Comment Heading"
                    if not comment_head_tag:
                        raise Exception("Comment heading tag not found")
                except Exception as e:
                    commentHead = "No Comment Heading"

                try:
                    comtag = commentbox.div.div.find_all('div', {'class': ''})
                    custComment = comtag[0].div.text if comtag and comtag[0].div else "No Comment"
                    if not comtag or not comtag[0].div:
                        raise Exception("Comment text not found")
                except Exception as e:
                    custComment = "No Comment"


                mydict = {
                    "Product": searchString,
                    "Name": name,
                    "Rating": rating,
                    "CommentHead": commentHead,
                    "Comment": custComment
                }
                reviews.append(mydict)
            logging.info("extracted information is appended to the list reviews")
            logging.info("creating a 'Dataframe' from extracted information")
            df = pd.DataFrame(reviews)
            df.to_csv(f"{searchString}.csv", index=False)
            logging.info(f"saving 'Dataframe' as [{searchString}.csv]")

            logging.info(f"{'*' * 10}Review_Flask-Scrapper-2025is Completed{'*' * 10}")
            return render_template('results.html', reviews=reviews[0:(len(reviews) - 1)])

        except Exception as e:
            raise ReviewException(e,sys) from e
>>>>>>> fe0a16e ( Added exception , logger ,Procfile ,templates ,test)

    # return render_template('results.html')

    else:
        return render_template('index.html')

if __name__ == "__main__":
<<<<<<< HEAD
    #app.run(host='127.0.0.1', port=8000, debug=True)
    port = int(os.environ.get("PORT", 5000))  # Get port from Heroku, default to 5000 locally
    app.run(host="0.0.0.0", port=port, debug=True)
=======
    app.run(host='127.0.0.1', port=8000, debug=True)
    # port = int(os.environ.get("PORT", 5000))  # Get port from Heroku, default to 5000 locally
    # app.run(host="0.0.0.0", port=port, debug=True)
>>>>>>> fe0a16e ( Added exception , logger ,Procfile ,templates ,test)




<<<<<<< HEAD
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
=======
    # TASK try to take search string from postman and try to load that entire data into pandas,sql,mongoDB

    # x = None
    # hasattr(x, 'div')  # False
    #
    # from bs4 import BeautifulSoup
    #
    # html = "<div><p>Hello</p></div>"
    # soup = BeautifulSoup(html, "html.parser")
    # tag = soup.find('div')
    #
    # hasattr(tag, 'text')  # True
    # hasattr(tag, 'div')  # True (since tag.div exists)
>>>>>>> fe0a16e ( Added exception , logger ,Procfile ,templates ,test)
