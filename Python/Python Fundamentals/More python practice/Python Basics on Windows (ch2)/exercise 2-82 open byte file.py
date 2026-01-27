with open(r'C:\Users\David\OneDrive\Desktop\ex82_horse.jpg', 'rb') as horse_pic:
          horse_pic.seek(2)
          horse_pic.seek(4)
          horse_pic.seek(0)
          print(horse_pic.tell())
          print(horse_pic.mode)
          data = horse_pic.read(10)
          print(data)
          
