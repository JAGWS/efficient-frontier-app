import pandas as pd
import numpy as np

import io


class Mercado():
    def __init__(self, archivo) -> None:
        excel = io.BytesIO(archivo)

        datos_esperados = pd.read_excel(excel, sheet_name="Datos esperados")
        datos_esperados = datos_esperados.rename({datos_esperados.columns[0]:'Datos'}, axis=1).set_index('Datos')
        self.nombres = datos_esperados.columns.tolist()

        mat_cov = pd.read_excel(excel, sheet_name="Matriz de covarianzas")
        mat_cov = mat_cov.rename({mat_cov.columns[0]:'Mat. cov.'}, axis=1).set_index('Mat. cov.')

        # Chequear tipo de dato
        self.rentabilidades = datos_esperados.iloc[0, :].tolist()

        if isinstance(self.rentabilidades[0], str):
            self.rentabilidades = [10**(-2)*float(x[:-1]) for x in self.rentabilidades]
        else:
            self.rentabilidades = [float(x) for x in self.rentabilidades]
            
        self.mat_covarianzas = mat_cov.to_numpy()

        # Chequear 'Histórico' o 'Esperado' y cambiar matriz de covarianzas
        clase = pd.read_excel(excel, sheet_name="Datos esperados", usecols="A").columns[0]

        if clase == "Esperado": # Modificar matriz de covarianzas
            np.fill_diagonal(self.mat_covarianzas, (datos_esperados.iloc[1, :])**2/365)


    def __str__(self) -> str:
        strr = "Lista de activos: "
        for n in self.nombres:
            strr += n + " "
        return strr 
    

    def get_pesos_distr(self):
        n_activos = len(self.nombres)
        st = self.__get_step(n_activos)

        variables = ['x'+str(i+1) for i in range(n_activos-1)]

        instruccion = 'pd.DataFrame([('
        instruccion += ', '.join(variables)+', '
        instruccion += '1-('+('+').join(variables)+')) '
        instruccion += ' '.join(['for '+var+' in np.arange(0, 1-('+ self.__return_str_vars_anteriores(variables, variables.index(var)) +')+'+str(st)+', '+str(st)+')' for var in variables])
        instruccion += '], columns=[*nombres])'

        t_pesos = eval(instruccion).to_numpy()
        
        return t_pesos


    def __get_step(num):
        steps = [0.005, 0.02, 0.05, 0.05, 0.1, 0.1, 0.1, 0.1, 0.125, 0.125, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]

        if num < 3:
            raise Exception("El número de activos debe ser mayor de 2") # TODO Mandar una alerta a través de Django... seguramente en la validación del form
        
        if num <= 20:
            return steps[num-3]
        else: 
            return 0.5


    def __return_str_vars_anteriores(t_variables, indice):
        if indice == 0:
            return '0'
        else:
            return '+'.join(t_variables[:indice])



def vol_cartera(pesos, mat_cov):
    return np.sqrt(365*(np.array(pesos) @ np.array(mat_cov) @ np.array(pesos)))


def rent_cartera(pesos, rent_anu):
    ddf = np.array(pesos).dot(np.array(rent_anu))
    return ddf


def sharpe(rent, vol):
    return rent/vol