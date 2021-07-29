
import random


when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan','Once upon a time','several years ago','ages ago','many years before','few years back','well before','at an earlier time','couple of years ago','earlier']

who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat','a man','elephant','a child','a women']

name = ['Ali','daniel' ,'puja','Rohan','vivek','mohan','roshan','sita','maya','mira','mahesh','krish']

residence = ['Barcelona','India', 'Germany', 'Mumbai', 'England','Pune','Jaipur','Delhi','Aurangabad','America','Japan','China','Pakistan','UK','Paris','Landon']

went = ['cinema', 'university','seminar', 'school', 'laundry','collage','Hospital','cloub house',"friend's home"]

happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book','fight with friends','eate snakes','learn new thing']


print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))