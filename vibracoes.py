import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



corbg= 'gainsboro'
lim= 2*np.pi
dt = 0.01

root = tk.Tk()
root.title('Vibrações')
root.config(bg= corbg)

def btn_apagar():
    a11.delete(0, tk.END)
    a12.delete(0, tk.END)
    a21.delete(0, tk.END)
    a22.delete(0, tk.END)

    msg_rodape.set("Créditos: Daniel Awada")
    t41.config(bg=corbg)

def btn_calcular():
    try:
        fn = float(a11.get())
        cc = float(a12.get())
        pos0= float(a21.get())
        vel0= float(a22.get())

    except ValueError:
        msg_rodape.set("As entradas devem ser numéricas!")
        t41.config(bg= 'red')
        y=0*t
        ax.set_ylim(-0.055, 0.055)
    else:
        msg_rodape.set("Créditos: Daniel Awada")
        t41.config(bg= corbg)
        y = vibes(fn, cc, pos0, vel0)
        ax.set_ylim(y.min(), y.max())
    finally:
        line1.set_ydata(y)
        fig.canvas.draw()


def vibes(fn, cc, pos0, vel0):
    fn = fn * 2 * np.pi
    t = np.arange(0.0, lim, dt)
    delta = fn * cc

    if pos0 == 0 and vel0 == 0:
        y = 0 * t

    elif cc < 1:
        v = fn * np.sqrt(1 - cc ** 2)
        C1 = pos0
        C2 = (delta * pos0 + vel0) / v
        C = np.sqrt(C1 ** 2 + C2 ** 2)
        if C2 < 0:  # condição para arrumar bug quando a velocidade inical é negativa
            C *= -1
        if C2 == 0:  # condição para evitar mensagem de erro de divisão por 0
            phi = np.pi / 2 * pos0 / np.abs(pos0)
        else:
            phi = np.arctan(C1 / C2)

        y = C * np.exp(-1 * delta * t) * np.sin(v * t + phi)

    elif cc == 1:
        A = pos0
        B = vel0 + fn * pos0

        y = (A + B * t) * np.exp(-1 * fn * t)

    elif cc > 1:
        gama = fn * np.sqrt(cc ** 2 - 1)
        lambda1 = -1 * delta + gama
        lambda2 = -1 * delta - gama
        A = (vel0 - lambda2 * pos0) / (lambda1 - lambda2)
        B = (lambda1 * pos0 - vel0) / (lambda1 - lambda2)

        y = np.exp(-1 * delta * t) * (A * np.exp(gama * t) + B * np.exp(-1 * gama * t))

    return (y)

#Título
tit = tk.Frame(root)
tit.grid(row=0, columnspan=3)

t0= tk.Label(tit, text="Simulação de Sistema MCK", bg= corbg)

t0.grid(row=0)

#wcc
wcc = tk.Frame(root, bg= corbg, bd=2, relief="groove")
wcc.grid(row=1, column=0, pady=5)


t11=tk.Label(wcc, text='Frequência natural [Hz]', bg=corbg)
a11 = tk.Entry(wcc)
t12=tk.Label(wcc, text='Razão de amortecimento', bg= corbg)
a12 = tk.Entry(wcc)

t11.grid(row=0, column=0)
a11.grid(row=0, column=1)
t12.grid(row=1, column=0)
a12.grid(row=1, column=1)

#condicoes iniciais
inic= tk.Frame(root, bg=corbg, bd=2, relief="groove")
inic.grid(row=1, column= 1, pady=5)


t21=tk.Label(inic, text='Posição inicial [m]', bg= corbg)
a21 = tk.Entry(inic)
t22=tk.Label(inic, text='Velocidade inicial [m/s]', bg= corbg)
a22 = tk.Entry(inic)

t21.grid(row=0, column=0)
a21.grid(row=0, column=1)
t22.grid(row=1, column=0)
a22.grid(row=1, column=1)

#botoes
btn= tk.Frame(root, bg=corbg)
btn.grid(row=2, columnspan=2, pady=5)

btn1= tk.Button(btn, text="Calcular", bg=corbg, command=btn_calcular)
btn2= tk.Button(btn, text="Apagar", bg=corbg, command= btn_apagar)

btn1.grid(row= 0, column=0)
btn2.grid(row= 0, column=1)


#gráfico
t= np.arange(0, lim, 0.01)
y= 0*t
fig = plt.Figure(figsize=(6, 3), dpi=100)
ax= fig.add_subplot(111)
line1, = ax.plot(t, y)

grafico = FigureCanvasTkAgg(fig, master=root)
grafico.get_tk_widget().grid(row=3, columnspan=2)

#image= tk.Frame(root)
#image.grid(row=3, columnspan=2, pady=5)

#canvas.draw()
#graph= tk.Canvas(image, width=600, height=200, bg='white')
#graph.grid(row=0)

#Rodapé
rod = tk.Frame(root)
rod.grid(row=4, columnspan=2)

msg_rodape= tk.StringVar()
t41= tk.Label(rod, textvariable=msg_rodape, bg= corbg)
msg_rodape.set("Créditos: Daniel Awada")

t41.grid(row=0)

root.mainloop()
