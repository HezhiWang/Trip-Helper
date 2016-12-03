"""

from reportlab.pdfgen import canvas


def hello(c):
  c.drawString(100,100,"Hello World")

c = canvas.Canvas("hello.pdf")
hello(c)
c.showPage()
c.save()
"""


from reportlab.pdfgen import canvas
 
c = canvas.Canvas("hello.pdf")
c.drawString(100,750,"Welcome to Reportlab!")
c.save()