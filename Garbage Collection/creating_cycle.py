def create_cycle():

  #create a list x
  x=[]

  #a reference cycle created here as x containd reference to self
  x.append(x)

create_cycle()  
