import numpy as np
from gnuradio import gr
import math

class blk(gr.sync_block):  
    """This block is a CE VCO or baseband VCO and works as following: ….. 
    La primera parte declaramos la frecuencia de la portadora, la frecuencia de muestreo
    En la segunda pate declaramos los valores de entrada, la salida es el producto del primer valor de entrada multiplicada por euler elevado a nuestro segundo valor de entrada por j, esta sera nuestra parte compleja"""

    def __init__(self,):  
        gr.sync_block.__init__(
            self,
            name='e_CE_VCO_fc',   
            in_sig=[np.float32, np.float32],
            out_sig=[np.complex64]
        )
        
    def work(self, input_items, output_items):
        A=input_items[0]
        Q=input_items[1]
        y=output_items[0]
        N=len(A)
        y[:]=A*np.exp(1j*Q)
        return len(output_items[0])
