import pyodbc

#科
class Family:
    def __init__(self, family_id, family_name):
        self.family_id = family_id
        self.family_name = family_name
#属
class Genus:
    def __init__(self, genus_id, genus_name):
        self.genus_id = genus_id
        self.genus_name = genus_name
#种
class Species:
    def __init__(self, species_id, characteristics, species_name, environment, diseases, alias, value, cultivation):
        self.species_id = species_id
        self.characteristics = characteristics
        self.species_name = species_name
        self.environment = environment
        self.diseases = diseases
        self.alias = alias
        self.value = value
        self.cultivation = cultivation
#省
class Province:
    def __init__(self, province_id, province_name):
        self.province_id = province_id
        self.province_name = province_name
#市
class City:
    def __init__(self, city_id, city_name):
        self.city_id = city_id
        self.city_name = city_name
#县
class County:
    def __init__(self, county_id, county_name):
        self.county_id = county_id
        self.county_name = county_name
##植物信息
class plant:
    def __init__(self,plant_id,plant_name):
         self.plant_id = plant_id
         self.plant_name = plant_name

# 其他实体类（例如属于科属、属种、省分布、市分布、县分布）类似定义
import pymssql
class BaseDAO:
    def __init__(self):
        self.connection = pymssql.connect(
            server='127.0.0.1',  # 或您的数据库服务器地址
            user='sa',  # 您的数据库用户名
            password='123456',  # 您的数据库密码
            database='plant'  # 您的数据库名称
        )
        self.cursor = self.connection.cursor(as_dict=True)
#配图
class picture:
    def __init__(self,picture_id,picture_spot,picture_miaoshu,picture_people):
        self.picture_id = picture_id
        self.picture_spot = picture_spot
        self.picture_miaoshu = picture_miaoshu
        self.picture_people = picture_people




class PictureDAO(BaseDAO):
    def get_picture_route(self,plant_name):
        query = '''
            SELECT [配图].[配图存储路径]
            FROM [植物信息]
            JOIN [配有] ON [植物信息].[植物编号] = [配有].[植物编号]
            JOIN [配图] ON [配有].[配图编号] = [配图].[配图编号]
            WHERE [植物信息].[植物名称] = %s
        '''
        self.cursor.execute(query, (plant_name,))
        result = self.cursor.fetchone()
        return result['配图存储路径'] if result else None
#科
class FamilyDAO(BaseDAO):
    def insert_family1(self, family):
        query = "INSERT INTO 科 (科ID, 科名) VALUES (?, ?)"
        values = (family.family_id, family.family_name)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_family_by_name(self, family_name):
        query = "SELECT * FROM 科 WHERE 科名 = ?"
        self.cursor.execute(query, (family_name,))
        row = self.cursor.fetchone()
        if row:
            return Family(row[0], row[1])
        return None
#根据科名找省市县
    def get_locations_by_family_name(self, family_name):
        query = '''
        SELECT 省.省名, 市.市名, 县.县名
        FROM 科
        INNER JOIN 属于科属 ON 科.科ID = 属于科属.科ID
        INNER JOIN 属 ON 属于科属.属ID = 属.属ID
        INNER JOIN 属于属种 ON 属.属ID = 属于属种.属ID
        INNER JOIN 种 ON 属于属种.种ID = 种.种ID
        INNER JOIN 县分布 ON 种.种ID = 县分布.种ID
        INNER JOIN 县 ON 县分布.县ID = 县.县ID
        INNER JOIN 市分布 ON 县.县ID = 市分布.县ID
        INNER JOIN 市 ON 市分布.市ID = 市.市ID
        INNER JOIN 省分布 ON 市.市ID = 省分布.市ID
        INNER JOIN 省 ON 省分布.省ID = 省.省ID
        WHERE 科.科名 = %s
        '''
        self.cursor.execute(query, (family_name,))
        rows = self.cursor.fetchall()
        return [(row['省名'], row['市名'], row['县名']) for row in rows] if rows else []
#省
#     def get_provinces_by_family_name(self, family_name):
#         query = '''
#         SELECT DISTINCT 省.省名
#         FROM 科
#         INNER JOIN 属于科属 ON 科.科ID = 属于科属.科ID
#         INNER JOIN 属 ON 属于科属.属ID = 属.属ID
#         INNER JOIN 属于属种 ON 属.属ID = 属于属种.属ID
#         INNER JOIN 种 ON 属于属种.种ID = 种.种ID
#         INNER JOIN 县分布 ON 种.种ID = 县分布.种ID
#         INNER JOIN 县 ON 县分布.县ID = 县.县ID
#         INNER JOIN 市分布 ON 县.县ID = 市分布.县ID
#         INNER JOIN 市 ON 市分布.市ID = 市.市ID
#         INNER JOIN 省分布 ON 市.市ID = 省分布.市ID
#         INNER JOIN 省 ON 省分布.省ID = 省.省ID
#         WHERE 科.科名 = %s
#         '''
#         self.cursor.execute(query, (family_name,))
#         rows = self.cursor.fetchall()
#         return [row['省名'] for row in rows] if rows else []
# #找市
    # def get_cities_by_family_name(self, family_name):
    #     query = '''
    #     SELECT DISTINCT 市.市名
    #     FROM 科
    #     INNER JOIN 属于科属 ON 科.科ID = 属于科属.科ID
    #     INNER JOIN 属 ON 属于科属.属ID = 属.属ID
    #     INNER JOIN 属于属种 ON 属.属ID = 属于属种.属ID
    #     INNER JOIN 种 ON 属于属种.种ID = 种.种ID
    #     INNER JOIN 县分布 ON 种.种ID = 县分布.种ID
    #     INNER JOIN 县 ON 县分布.县ID = 县.县ID
    #     INNER JOIN 市分布 ON 县.县ID = 市分布.县ID
    #     INNER JOIN 市 ON 市分布.市ID = 市.市ID
    #     WHERE 科.科名 = %s
    #     '''
    #     self.cursor.execute(query, (family_name,))
    #     rows = self.cursor.fetchall()
    #     return [row['市名'] for row in rows] if rows else []

#找县
    # def get_counties_by_family_name(self, family_name):
    #     query = '''
    #     SELECT 县.县名
    #     FROM 科
    #     INNER JOIN 属于科属 ON 科.科ID = 属于科属.科ID
    #     INNER JOIN 属 ON 属于科属.属ID = 属.属ID
    #     INNER JOIN 属于属种 ON 属.属ID = 属于属种.属ID
    #     INNER JOIN 种 ON 属于属种.种ID = 种.种ID
    #     INNER JOIN 县分布 ON 种.种ID = 县分布.种ID
    #     INNER JOIN 县 ON 县分布.县ID = 县.县ID
    #     WHERE 科.科名 = %s
    #     '''
    #     self.cursor.execute(query, (family_name,))
    #     rows = self.cursor.fetchall()
    #     return [row['县名'] for row in rows] if rows else []
#根据科名找属名
    def get_genus_by_family_name(self, family_name):
        query = '''
        SELECT DISTINCT [属].[属名]
        FROM [科]
        JOIN [属于科属] ON [科].[科ID] = [属于科属].[科ID]
        JOIN [属] ON [属于科属].[属ID] = [属].[属ID]
        WHERE [科].[科名] = %s
        '''
        self.cursor.execute(query, (family_name,))
        rows = self.cursor.fetchall()
        return [row['属名'] for row in rows] if rows else []
#根据科名找属名和种名（不输出种的详细信息）
    def get_species_and_genus_by_family_name(self, family_name):
        query = '''
        SELECT [属].[属名], [种].[种名]
        FROM [科]
        JOIN [属于科属] ON [科].[科ID] = [属于科属].[科ID]
        JOIN [属] ON [属于科属].[属ID] = [属].[属ID]
        JOIN [属于属种] ON [属].[属ID] = [属于属种].[属ID]
        JOIN [种] ON [属于属种].[种ID] = [种].[种ID]
        WHERE [科].[科名] = %s
        '''
        self.cursor.execute(query, (family_name,))
        rows = self.cursor.fetchall()
        return [(row['属名'], row['种名']) for row in rows] if rows else []
#根据科名找属名和种名植物名
    def get_plant_species_and_genus_by_family_name(self, family_name):
        query = '''
        SELECT [属].[属名], [种].[种名], [植物信息].[植物名称]
        FROM [科]
        JOIN [属于科属] ON [科].[科ID] = [属于科属].[科ID]
        JOIN [属] ON [属于科属].[属ID] = [属].[属ID]
        JOIN [属于属种] ON [属].[属ID] = [属于属种].[属ID]
        JOIN [种] ON [属于属种].[种ID] = [种].[种ID]
        JOIN [属于植物信息] ON [种].[种ID] = [属于植物信息].[种ID]
        JOIN [植物信息] ON [属于植物信息].[植物编号] = [植物信息].[植物编号]
        WHERE [科].[科名] = %s
        '''
        self.cursor.execute(query, (family_name,))
        rows = self.cursor.fetchall()
        return [(row['属名'], row['种名'], row['植物名称']) for row in rows] if rows else []

#插入科名
    def insert_family(self, family):
        query = "INSERT INTO 科 (科ID, 科名) VALUES (%s, %s)"
        values = (family.family_id, family.family_name)
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            print("科名插入成功。")
        except Exception as e:
            print(f"插入科名时发生错误：{e}")


#属
class GenusDAO(BaseDAO):
    def insert_genus(self, genus):
        query = "INSERT INTO 属 (属ID, 属名) VALUES (%s, %s)"
        values = (genus.genus_id, genus.genus_name)
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            print("科名插入成功。")
        except Exception as e:
            print(f"插入科名时发生错误：{e}")

    def get_genus_by_name(self, genus_name):
        query = "SELECT * FROM 属 WHERE 属名 = ?"
        self.cursor.execute(query, (genus_name,))
        row = self.cursor.fetchone()
        if row:
            return Genus(row[0], row[1])
        return None

    #省市县
    def get_locations_by_genus_name(self, genus_name):
        query = '''
        SELECT 省.省名, 市.市名, 县.县名
        FROM 属
        INNER JOIN 属于属种 ON 属.属ID = 属于属种.属ID
        INNER JOIN 种 ON 属于属种.种ID = 种.种ID
        INNER JOIN 县分布 ON 种.种ID = 县分布.种ID
        INNER JOIN 县 ON 县分布.县ID = 县.县ID
        INNER JOIN 市分布 ON 县.县ID = 市分布.县ID
        INNER JOIN 市 ON 市分布.市ID = 市.市ID
        INNER JOIN 省分布 ON 市.市ID = 省分布.市ID
        INNER JOIN 省 ON 省分布.省ID = 省.省ID
        WHERE 属.属名 = %s
        '''
        self.cursor.execute(query, (genus_name,))
        rows = self.cursor.fetchall()
        return [(row['省名'], row['市名'], row['县名']) for row in rows] if rows else []
#不输出详细信息版本
    def get_species_by_genus_name(self, genus_name):
        query = '''
        SELECT DISTINCT 种.种名
        FROM 属
        INNER JOIN 属于属种 ON 属.属ID = 属于属种.属ID
        INNER JOIN 种 ON 属于属种.种ID = 种.种ID
        WHERE 属.属名 = %s
        ORDER BY 种.种名
        '''
        self.cursor.execute(query, (genus_name,))
        rows = self.cursor.fetchall()
        return [row['种名'] for row in rows] if rows else []

    def get_plant_species_by_genus_name(self, genus_name):
        query = '''
        SELECT DISTINCT 种.种名, 植物信息.植物名称
        FROM 属
        INNER JOIN 属于属种 ON 属.属ID = 属于属种.属ID
        INNER JOIN 种 ON 属于属种.种ID = 种.种ID
        LEFT JOIN 属于植物信息 ON 种.种ID = 属于植物信息.种ID
        LEFT JOIN 植物信息 ON 属于植物信息.植物编号 = 植物信息.植物编号
        WHERE 属.属名 = %s
        ORDER BY 种.种名, 植物信息.植物名称
        '''
        self.cursor.execute(query, (genus_name,))
        rows = self.cursor.fetchall()
        return [(row['种名'], row.get('植物名称')) for row in rows] if rows else []

#种
class SpeciesDAO(BaseDAO):
    def insert_species(self, species):
        query = "INSERT INTO 种 (种ID, 形态特征, 种名, 生长环境, 病名, 别名, 应用价值, 栽培要点) VALUES (%d, %s, %s, %s, %s, %s, %s, %s)"
        values = (species.species_id, species.characteristics, species.species_name, species.environment, species.diseases, species.alias, species.value, species.cultivation)
        self.cursor.execute(query, values)
        self.connection.commit()
#通过种名查找县
    # def get_counties_by_species_name(self, species_name):
    #     query = '''
    #     SELECT 县.县名, 县.县ID
    #     FROM 种
    #     JOIN 县分布 ON 种.种ID = 县分布.种ID
    #     JOIN 县 ON 县分布.县ID = 县.县ID
    #     WHERE 种.种名 = %s
    #     '''
    #     self.cursor.execute(query, (species_name,))
    #     rows = self.cursor.fetchall()
    #     if not rows:
    #         print("未找到与该种名匹配的县信息。")
    #         return []
    #     return [County(row['县ID'], row['县名']) for row in rows]

#通过种名查找市
    # def get_cities_by_species_name(self, species_name):
    #         query = '''
    #         SELECT 市.市名
    #         FROM 种
    #         JOIN 县分布 ON 种.种ID = 县分布.种ID
    #         JOIN 县 ON 县分布.县ID = 县.县ID
    #         JOIN 市分布 ON 县.县ID = 市分布.县ID
    #         JOIN 市 ON 市分布.市ID = 市.市ID
    #         WHERE 种.种名 = %s
    #         '''
    #         self.cursor.execute(query, (species_name,))
    #         rows = self.cursor.fetchall()
    #         return [row['市名'] for row in rows] if rows else []



    # def get_provinces_by_species_name(self, species_name):
    #         query = '''
    #         SELECT 省.省名
    #         FROM 种
    #         JOIN 县分布 ON 种.种ID = 县分布.种ID
    #         JOIN 县 ON 县分布.县ID = 县.县ID
    #         JOIN 市分布 ON 县.县ID = 市分布.县ID
    #         JOIN 市 ON 市分布.市ID = 市.市ID
    #         JOIN 省分布 ON 市.市ID = 省分布.市ID
    #         JOIN 省 ON 省分布.省ID = 省.省ID
    #         WHERE 种.种名 = %s
    #         '''
    #         self.cursor.execute(query, (species_name,))
    #         rows = self.cursor.fetchall()
    #         return [row['省名'] for row in rows] if rows else []

    #通过种名查找省市县
    def get_locations_by_species_name(self, species_name):
        query = '''
        SELECT 省.省名, 市.市名, 县.县名
        FROM 种
        JOIN 县分布 ON 种.种ID = 县分布.种ID
        JOIN 县 ON 县分布.县ID = 县.县ID
        JOIN 市分布 ON 县.县ID = 市分布.县ID
        JOIN 市 ON 市分布.市ID = 市.市ID
        JOIN 省分布 ON 市.市ID = 省分布.市ID
        JOIN 省 ON 省分布.省ID = 省.省ID
        WHERE 种.种名 = %s
        '''
        self.cursor.execute(query, (species_name,))
        rows = self.cursor.fetchall()
        return [(row['省名'], row['市名'], row['县名']) for row in rows] if rows else []



# 根据种名进行模糊查询
    def get_species_by_name_fuzzy(self, species_name):
        query = "SELECT * FROM 种 WHERE 种名 LIKE %s"
        self.cursor.execute(query, ('%' + species_name + '%',))
        rows = self.cursor.fetchall()
        return [Species(row['种ID'], row['形态特征'], row['种名'], row['生长环境'], row['病名'], row['别名'],
                        row['应用价值'], row['栽培要点']) for row in rows]

    # 更新种信息
    def update_species(self, species):
        query = "UPDATE 种 SET 形态特征 = %s, 种名 = %s, 生长环境 = %s, 病名 = %s, 别名 = %s, 应用价值 = %s, 栽培要点 = %s WHERE 种ID = %d"
        values = (species.characteristics, species.species_name, species.environment, species.diseases, species.alias,
                  species.value, species.cultivation, species.species_id)
        self.cursor.execute(query, values)
        self.connection.commit()

    #删除种信息
    def delete_species(self, species_id):
        query = "DELETE FROM 种 WHERE 种ID = %d"
        self.cursor.execute(query, (species_id,))
        self.connection.commit()
        #根据种名或者别名来查询信息
    def get_species_info_by_name_or_alias(self, name_or_alias):
            query = '''
                SELECT 形态特征, 生长环境, 病名, 别名, 应用价值, 栽培要点
                FROM 种
                WHERE 种名 = %s OR 别名 = %s
            '''
            self.cursor.execute(query, (name_or_alias, name_or_alias))
            row = self.cursor.fetchone()
            if row:
                return {
                    '形态特征': row['形态特征'],
                    '生长环境': row['生长环境'],
                    '病名': row['病名'],
                    '别名': row['别名'],
                    '应用价值': row['应用价值'],
                    '栽培要点': row['栽培要点']
                }
            return None


    def get_plant_names_by_species_name(self, species_name):
        query = '''
        SELECT 植物信息.植物名称
        FROM 种
        LEFT JOIN 属于植物信息 ON 种.种ID = 属于植物信息.种ID
        LEFT JOIN 植物信息 ON 属于植物信息.植物编号 = 植物信息.植物编号
        WHERE 种.种名 = %s
        ORDER BY 植物信息.植物名称
        '''
        self.cursor.execute(query, (species_name,))
        rows = self.cursor.fetchall()
        return [row['植物名称'] for row in rows] if rows else []




         # 根据种名或者别名来查询信息

    def get_species_info_by_name_or_alias(self, name_or_alias):
        query = '''
                SELECT 形态特征, 生长环境, 病名, 别名, 应用价值, 栽培要点
                FROM 种
                WHERE 种名 = %s OR 别名 = %s
            '''
        self.cursor.execute(query, (name_or_alias, name_or_alias))
        row = self.cursor.fetchone()
        if row:
            return {
                '形态特征': row['形态特征'],
                '生长环境': row['生长环境'],
                '病名': row['病名'],
                '别名': row['别名'],
                '应用价值': row['应用价值'],
                '栽培要点': row['栽培要点']
            }
        return None

        # 根据生长环境进行模糊查询

    def get_species_names_by_environment_fuzzy(self, environment):
        query = "SELECT 种名 FROM 种 WHERE 生长环境 LIKE %s"
        pattern = f'%{environment}%'
        self.cursor.execute(query, (pattern,))
        rows = self.cursor.fetchall()
        return [row['种名'] for row in rows]

        # 更新种信息

    def update_species(self, species):
        query = "UPDATE 种 SET 形态特征 = %s,生长环境 = %s, 病名 = %s, 别名 = %s, 应用价值 = %s, 栽培要点 = %s WHERE 种名 = %s"
        values = (species.characteristics, species.environment, species.diseases, species.alias,
                  species.value, species.cultivation, species.species_name)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_species_by_name(self, species_name):
        query = "DELETE FROM 种 WHERE 种名 = %s"
        self.cursor.execute(query, (species_name,))
        self.connection.commit()
        return self.cursor.rowcount

    def insert_species(self, species):
        query = "INSERT INTO 种 (种ID, 形态特征, 种名, 生长环境, 病名, 别名, 应用价值, 栽培要点) VALUES (%d, %s, %s, %s, %s, %s, %s, %s)"
        values = (
        species.species_id, species.characteristics, species.species_name, species.environment, species.diseases,
        species.alias, species.value, species.cultivation)
        self.cursor.execute(query, values)
        self.connection.commit()



#植物信息
class plantDAO(BaseDAO):
    def get_shu_by_plant_name(self,plant_name):
        query = '''
            SELECT [属].[属名] 
            FROM [植物信息] 
            JOIN [属于植物信息] ON [植物信息].[植物编号] = [属于植物信息].[植物编号] 
            JOIN [种] ON [属于植物信息].[种ID] = [种].[种ID]
            JOIN [属于属种] ON [属于属种].[种ID] = [种].[种ID] 
            JOIN [属] ON [属于属种].[属ID] = [属].[属ID] 
            WHERE [植物信息].[植物名称] = %s
        '''
        self.cursor.execute(query,(plant_name,))
        result = self.cursor.fetchone()
        return result['属名'] if result else None

    def get_zhong_by_plant_name(self,plant_name):
        query = '''
            SELECT [种].[种名] 
            FROM [植物信息] 
            JOIN [属于植物信息] ON [植物信息].[植物编号] = [属于植物信息].[植物编号] 
            JOIN [种] ON [属于植物信息].[植物编号] = [种].[种ID] 
            WHERE [植物信息].[植物名称] = %s
        '''
        self.cursor.execute(query,(plant_name,))
        result = self.cursor.fetchone()
        return result['种名'] if result else None

    def get_ke_by_plant_name(self,plant_name):
        query = '''
            SELECT [科].[科名] 
            FROM [植物信息] 
            JOIN [属于植物信息] ON [植物信息].[植物编号] = [属于植物信息].[植物编号] 
            JOIN [种] ON [属于植物信息].[种ID] = [种].[种ID]
            JOIN [属于属种] ON [属于属种].[种ID] = [种].[种ID] 
            JOIN [属] ON [属于属种].[属ID] = [属].[属ID] 
            JOIN [属于科属] ON [属于科属].[属ID] = [属].[属ID] 
            JOIN [科] ON [属于科属].[科ID] = [科].[科ID] 
            WHERE [植物信息].[植物名称] = %s
        '''
        self.cursor.execute(query,(plant_name,))
        result = self.cursor.fetchone()
        return result['科名'] if result else None

    def get_locations_by_plant_name(self, plant_name):
        query = '''
        SELECT 省.省名, 市.市名, 县.县名
        FROM [植物信息]
        JOIN [属于植物信息] ON [植物信息].[植物编号] = [属于植物信息].[植物编号]
        JOIN [种] ON [属于植物信息].[种ID] = [种].[种ID]
        JOIN [属于属种] ON [种].[种ID] = [属于属种].[种ID]
        JOIN [属] ON [属于属种].[属ID] = [属].[属ID]
        JOIN [属于科属] ON [属].[属ID] = [属于科属].[属ID]
        JOIN [科] ON [属于科属].[科ID] = [科].[科ID]
        JOIN [县分布] ON [种].[种ID] = [县分布].[种ID]
        JOIN [县] ON [县分布].[县ID] = [县].[县ID]
        JOIN [市分布] ON [县].[县ID] = [市分布].[县ID]
        JOIN [市] ON [市分布].[市ID] = [市].[市ID]
        JOIN [省分布] ON [市].[市ID] = [省分布].[市ID]
        JOIN [省] ON [省分布].[省ID] = [省].[省ID]
        WHERE [植物信息].[植物名称] = %s
        '''
        self.cursor.execute(query, (plant_name,))
        rows = self.cursor.fetchall()
        return [(row['省名'], row['市名'], row['县名']) for row in rows] if rows else []
#根据种名或者别名来查询信息
    def get_species_info_by_name_or_alias(self, name_or_alias):
        query = '''
            SELECT 形态特征, 生长环境, 病名, 别名, 应用价值, 栽培要点
            FROM 种
            WHERE 种名 = %s OR 别名 = %s
        '''
        self.cursor.execute(query, (name_or_alias, name_or_alias))
        row = self.cursor.fetchone()
        if row:
            return {
                '形态特征': row['形态特征'],
                '生长环境': row['生长环境'],
                '病名': row['病名'],
                '别名': row['别名'],
                '应用价值': row['应用价值'],
                '栽培要点': row['栽培要点']
            }
        return None

    # 根据生长环境进行模糊查询
    def get_species_names_by_environment_fuzzy(self, environment):
        query = "SELECT 种名 FROM 种 WHERE 生长环境 LIKE %s"
        pattern = f'%{environment}%'
        self.cursor.execute(query, (pattern,))
        rows = self.cursor.fetchall()
        return [row['种名'] for row in rows]


    # 更新种信息
    def update_species(self, species):
        query = "UPDATE 种 SET 形态特征 = %s,生长环境 = %s, 病名 = %s, 别名 = %s, 应用价值 = %s, 栽培要点 = %s WHERE 种名 = %s"
        values = (species.characteristics, species.environment, species.diseases, species.alias,
                  species.value, species.cultivation, species.species_name)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_plant_by_name(self, plant_name):
        # 检查是否存在依赖的记录（如有需要先处理）

        # 执行删除操作
        query = "DELETE FROM 植物信息 WHERE 植物名称 = %s"
        self.cursor.execute(query, (plant_name,))
        self.connection.commit()
        return self.cursor.rowcount  # 返回受影响的行数


#建立视图查询
class FamilyGenusSpeciesDAO(BaseDAO):
    # ...

    def get_species_info_by_family_name(self, family_name):
        query = '''
        SELECT *
        FROM View_FamilyGenusSpeciesInfo
        WHERE 科名 = %s
        '''
        self.cursor.execute(query, (family_name,))
        rows = self.cursor.fetchall()
        return rows

    def get_species_info_by_genus_name(self, genus_name):
        query = '''
        SELECT *
        FROM View_FamilyGenusSpeciesInfo
        WHERE 属名 = %s
        '''
        self.cursor.execute(query, (genus_name,))
        rows = self.cursor.fetchall()
        return rows

# 类似地，为省、市、县及其分布实现DAO类
def main():
    plant_dao = plantDAO()

    # 假定植物名称为 "某植物"，请根据您的数据库实际情况进行修改
    plant_name = "二色补血草"

    # 调用 get_locations_by_plant_name 方法并打印结果
    locations = plant_dao.get_locations_by_plant_name(plant_name)
    if locations:
        print(f"植物名为 '{plant_name}' 的植物分布的省市县如下：")
        for province, city, county in locations:
            print(f"省：{province}, 市：{city}, 县：{county}")
    else:
        print(f"未找到植物名为 '{plant_name}' 的植物的分布信息。")



#通过科名去查找下属
def main2():
    family_dao = FamilyDAO()

    family_name = "白花丹科"  # 请根据您的数据库实际情况进行修改

    species_genus_pairs = family_dao.get_species_and_genus_by_family_name(family_name)
    for genus, species in species_genus_pairs:
        print(f"科名 '{family_name}' 下的属：{genus}")
        print(f"种：{species if species else '无'}")

    plant_species_genus_pairs = family_dao.get_plant_species_and_genus_by_family_name(family_name)
    for genus, species, plant_name in plant_species_genus_pairs:
        print(f"科名 '{family_name}' 下的属：{genus}, 种：{species if species else '无'}, 植物名称：{plant_name if plant_name else '无'}")
        print(f"种：{species if species else '无'}")
        print(f"植物名称：{plant_name if plant_name else '无'}")

def main3():
            genus_dao = GenusDAO()

            # 假定属名为 "某属"，请根据您的数据库实际情况进行修改
            genus_name = "补血草属"

            # 查询种
            species_names = genus_dao.get_species_by_genus_name(genus_name)
            print(f"属名为 '{genus_name}' 下的种有：{', '.join(species_names) if species_names else '无'}")

            # 查询种和植物名称
            plant_species_pairs = genus_dao.get_plant_species_by_genus_name(genus_name)
            for species, plant_name in plant_species_pairs:
                print(f"属名 '{genus_name}' 下的种：{species}")
                print(f"植物名称：{plant_name if plant_name else '无'}")


def main4():
    species_dao = SpeciesDAO()

    # 假定种名为 "某种"，请根据您的数据库实际情况进行修改
    species_name = "efg"

    # 查询植物名称
    plant_names = species_dao.get_plant_names_by_species_name(species_name)
    if plant_names:
        print(f"种名为 '{species_name}' 的植物名称有：{', '.join(plant_names)}")
    else:
        print(f"未找到种名为 '{species_name}' 的植物名称。")


def main5():
    species_dao = SpeciesDAO()
    environment = "阳光"
    species_names = species_dao.get_species_names_by_environment_fuzzy(environment)
    if species_names:
        print(f"根据生长环境 '{environment}' 模糊查询的种名：")
        for species_name in species_names:
          print(species_name)

def main6():
    species_dao = SpeciesDAO()

    species_name_to_delete = "efg"  # 假定要删除的种名

    # 执行删除操作
    result = species_dao.delete_species_by_name(species_name_to_delete)
    if result == -1:
        print(f"种名为 '{species_name_to_delete}' 的记录存在依赖关系，无法删除。")
    elif result > 0:
        print(f"成功删除了 {result} 行，种名为 '{species_name_to_delete}' 的记录。")
    else:
        print(f"没有找到种名为 '{species_name_to_delete}' 的记录，无法删除。")


def main7():
    new_species = Species(
        species_id=1005,
        characteristics="测试特征",
        species_name="测试种名2",
        environment="测试环境",
        diseases="测试病名",
        alias="测试别名",
        value="测试价值",
        cultivation="测试栽培要点"
    )
    species_dao = SpeciesDAO()
    species_dao.insert_species(new_species)

    species_info = species_dao.get_species_info_by_name_or_alias("测试种名2")
    if species_info:
        print("通过种名查询到的信息：", species_info)
    else:
        print("未找到相关信息。")
def main9():
    species_dao = SpeciesDAO()
    species_name_to_delete = "测试种名123"

    deleted_rows = species_dao.delete_species_by_name(species_name_to_delete)
    if deleted_rows > 0:
        print(f"成功删除了种名为 '{species_name_to_delete}' 的记录及其相关联的数据。")
    else:
        print(f"没有找到种名为 '{species_name_to_delete}' 的记录，无法删除。")

def main10():
    genus_dao = GenusDAO()
    new_family = Genus(1235, "测试科名")
    genus_dao.insert_genus(new_family)


def main11():
    dao = FamilyGenusSpeciesDAO()

    # 假定的科名和属名
    family_name = "白花丹科"
    genus_name = "补血草属"

    # 测试根据科名查询
    species_info_by_family = dao.get_species_info_by_family_name(family_name)
    print(f"科名 '{family_name}' 下的种信息：")
    for species in species_info_by_family:
        print(species)

    # 测试根据属名查询
    species_info_by_genus = dao.get_species_info_by_genus_name(genus_name)
    print(f"\n属名 '{genus_name}' 下的种信息：")
    for species in species_info_by_genus:
        print(species)




if __name__ == "__main__":
    main11()






