
#Read in the files first. 
top_html = open('./templates/top.html').read()
bottom_html = open("./templates/bottom.html").read()
index_html = open("./content/index.html").read()
contact_html = open("./content/contact.html").read()
portfolio_html = open("./content/portfolio.html").read()
proExperience_html = open("./content/proExperience.html").read()

# /Users/nunezj/Desktop/Kickstart/ResumeWebSite/MyResume/templates/top.html

#create the full webpages 
indexFull_html = top_html + index_html + bottom_html
contactFull_html = top_html + contact_html + bottom_html
portfolioFull_html = top_html + portfolio_html + bottom_html
proExperienceFull_html = top_html + proExperience_html + bottom_html


# output the create webpages into html files. 

open("./docs/index.html", "w+").write(indexFull_html)
open("./docs/contact.html", "w+").write(contactFull_html)
open("./docs/portfolio.html", "w+").write(portfolioFull_html)
open("./docs/proExperience.html", "w+").write(proExperienceFull_html)




