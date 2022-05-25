# img = [0] * 400
# rs = []
# i = 0
# x, y = 2, 1
# i = (40 * y) + (x * 4)
# print(i)
# while i<len(img):
#     rs.extend(img[i:i+20])
#     i += 40
#     if i == (40 * (y+5)) + (4 * (x)):
#         break
# print(len(img))
# print(len(rs))


#Row, Column format points
m1, m2 = 10, 10     #meatrix size
c1, c2 = 5, 5       #cropping size
p1, p2 = 2, 4       #staring points

img = [0] * (m1*m2*4)

i = (4 * p1 * m2) + (4 * p2)
rs = []

while i < len(img):
    rs.extend(img[i:i+(4*c2)])
    i += (m2 * 4)

    if i == (4 * p2) + ((c1 + p1) * 4 * m2):
        break

print(len(rs))