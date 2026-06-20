import threading
def evaluate_student(name,m1, m2, m3 ):
    total = m1 + m2 + m3
    avg = total/3
    if avg >= 40:
        result = "Pass"
    else:
        result = "Fail" 
    print(name, total, result)
n = int(input("enter number ofstudents"))  
threads=[]
for i in range(n):
    name, m1, m2, m3 = input().split()
    t = threading.Thread(
        target = evaluate_student, args=(name, int(m1), int(m2),int(m3)))
    threads.append(t) 
    t.start() 
      
for t in threads:
    t.join()
print("result processng completed")     



 
             
