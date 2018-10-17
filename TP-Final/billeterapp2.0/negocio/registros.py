from datos.registros import RegistroData

class RegistroLogic():

    @staticmethod
    def insert_one(registro):
        RegistroData.create_registro(registro)

    @staticmethod
    def get_by_id(registro_id):
        return RegistroData.get_by_id(registro_id)
    
    @staticmethod
    def update_registro(registro_id, registro):
        RegistroData.update_registro(registro_id, registro)

    @staticmethod
    def find_by_categoria(categoria):
        return RegistroData.find_by_categoria(categoria)

    @staticmethod
    def get_lasts_registers(userid, top):
        l = list(RegistroData.get_lasts_registers(userid, top))
        return l

    @staticmethod
    def get_balance(userid):
        montos = list(RegistroData.get_montos(userid))
        count = 0
        for m in montos:
            if m["tipo"] == "gasto":
                count = count - float(format(m["valor"], ".2f"))
            elif m["tipo"] == "ingreso":
                count = count + float(format(m["valor"], ".2f"))
        return count
    
    @staticmethod
    def get_sueldo(userid):
        try:
            sueldo = RegistroData.get_sueldo(userid)
            if sueldo is not None:
                return sueldo["valor"]
            else:
                return "No hay sueldos cargados"
        except ValueError as e:
            print("Error en la conversión de tipo de dato: {0}", format(e))

    @staticmethod
    def get_tipos(userid):
        cur = RegistroData.get_registros(userid)
        cat = {}
        for i in cur:
            a = i['tipo']
            if i['tipo'] in list(cat):
                cat[a] = cat[a] + i['valor']
            else:
                cat[a] = i['valor']
        print(cat)
        return cat

    @staticmethod
    def get_cats(userid, tipo):
        registros = RegistroData.get_categorias(userid, tipo)
        c = {}
        for r in registros:
            for categoria in r["categoria"]:
                if categoria in c:
                    c[categoria] += r["valor"]
                else: 
                    c[categoria] = r["valor"]
        return c

    @staticmethod
    def get_cats_names(userid, tipo):
        registros = RegistroData.get_categorias(userid, tipo)
        cat_nombres = []
        for r in registros:
            for categoria in r["categoria"]:
                if categoria not in cat_nombres:
                    cat_nombres.append(categoria)
        return cat_nombres
