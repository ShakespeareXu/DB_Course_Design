
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
    def __init__(self, species_id, characteristics, species_name, environment, alias, value, cultivation):
        self.species_id = species_id
        self.characteristics = characteristics
        self.species_name = species_name
        self.environment = environment
        #self.diseases = diseases
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

#植物信息
class plant:
    def __init__(self,plant_id,plant_name):
        self.plant_id = plant_id
        self.plant_name = plant_name

#配图
class picture:
    def __init__(self,picture_id,picture_spot,picture_miaoshu,picture_people):
        self.picture_id = picture_id
        self.picture_spot = picture_spot
        self.picture_miaoshu = picture_miaoshu
        self.picture_people = picture_people

# 其他实体类（例如属于科属、属种、省分布、市分布、县分布）类似定义
from unicodedata import name
from winreg import QueryInfoKey
import pymssql
class BaseDAO:
    def __init__(self):
        self.connection = pymssql.connect(
            server='127.0.0.1',  # 或您的数据库服务器地址
            user='sa',  # 您的数据库用户名
            password='123456',  # 您的数据库密码
            database='plant'  # 您的数据库名称
            , charset='UTF-8', tds_version="7.0"
        )
        self.cursor = self.connection.cursor(as_dict=True)

#配图
class PictureDAO(BaseDAO):
    # def get_picture_route(self,plant_name):
    #     query = '''
    #         SELECT [配图].[配图存储路径]
    #         FROM [植物信息]
    #         JOIN [配有] ON [植物信息].[植物编号] = [配有].[植物编号]
    #         JOIN [配图] ON [配有].[配图编号] = [配图].[配图编号]
    #         WHERE [植物信息].[植物名称] = %s
    #     '''
    #     self.cursor.execute(query, (plant_name,))
    #     result = self.cursor.fetchone()
    #     return result['配图存储路径'] if result else None
    # def get_picture_people(self,plant_name):
    #     query = '''
    #         SELECT [配图].[配图拍摄人]
    #         FROM [植物信息]
    #         JOIN [配有] ON [植物信息].[植物编号] = [配有].[植物编号]
    #         JOIN [配图] ON [配有].[配图编号] = [配图].[配图编号]
    #         WHERE [植物信息].[植物名称] = %s
    #     '''
    #     self.cursor.execute(query, (plant_name,))
    #     result = self.cursor.fetchone()
    #     return result['配图拍摄人'] if result else None
    # def get_picture_spot(self,plant_name):
    #     query = '''
    #         SELECT [配图].[配图拍摄地点]
    #         FROM [植物信息]
    #         JOIN [配有] ON [植物信息].[植物编号] = [配有].[植物编号]
    #         JOIN [配图] ON [配有].[配图编号] = [配图].[配图编号]
    #         WHERE [植物信息].[植物名称] = %s
    #     '''
    #     self.cursor.execute(query, (plant_name,))
    #     result = self.cursor.fetchone()
    #     return result['配图拍摄地点'] if result else None
    # def get_picture_miaoshu(self,plant_name):
    #     query = '''
    #         SELECT [配图].[配图描述]
    #         FROM [植物信息]
    #         JOIN [配有] ON [植物信息].[植物编号] = [配有].[植物编号]
    #         JOIN [配图] ON [配有].[配图编号] = [配图].[配图编号]
    #         WHERE [植物信息].[植物名称] = %s
    #     '''
    #     self.cursor.execute(query, (plant_name,))
    #     result = self.cursor.fetchone()
    #     return result['配图描述'] if result else None


    def get_all_pictures_by_species_id(self, species_id):
        query = '''
            SELECT [配图].[配图存储路径], [配图].[配图拍摄人], [配图].[配图拍摄地点], [配图].[配图描述]
            FROM [种]
            JOIN [属于植物信息] ON [种].[种ID] = [属于植物信息].[种ID]
            JOIN [植物信息] ON [属于植物信息].[植物编号] = [植物信息].[植物编号]
            JOIN [配有] ON [植物信息].[植物编号] = [配有].[植物编号]
            JOIN [配图] ON [配有].[配图编号] = [配图].[配图编号]
            WHERE [种].[种ID] = %s
        '''
        self.cursor.execute(query, (species_id,))
        results = self.cursor.fetchall()

        pictures_info = []
        for result in results:
            picture_info = {
                '配图存储路径': result['配图存储路径'],
                '配图拍摄人': result['配图拍摄人'],
                '配图拍摄地点': result['配图拍摄地点'],
                '配图描述': result['配图描述']
            }
            pictures_info.append(picture_info)

        return pictures_info



#科
class FamilyDAO(BaseDAO):
    def insert_family(self, family):
        query = "INSERT INTO 科 (科ID, 科名) VALUES (%s, %s)"
        values = (family.family_id, family.family_name)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_family_by_name(self, family_name):
        query = "SELECT * FROM 科 WHERE 科名 = %s"
        self.cursor.execute(query, (family_name,))
        row = self.cursor.fetchone()
        if row:
            return Family('科ID', '科名')
        return None

    # def get_plant_count_by_family(self,family_name):
    #     query = '''
    #         SELECT
    #             科.科名,
    #             COUNT(植物信息.植物编号) AS 植物数量
    #         FROM
    #             科
    #         JOIN
    #             属于科属 ON 科.科ID = 属于科属.科ID
    #         JOIN
    #             属 ON 属于科属.属ID = 属.属ID
    #         JOIN
    #             属于属种 ON 属.属ID = 属于属种.属ID
    #         JOIN
    #             种 ON 属于属种.种ID = 种.种ID
    #         JOIN
    #             属于植物信息 ON 种.种ID = 属于植物信息.种ID
    #         JOIN
    #             植物信息 ON 属于植物信息.植物编号 = 植物信息.植物编号
    #         GROUP BY
    #             科.科名;
    #     '''
    #     self.cursor.execute(query, (family_name,))
    #     result = self.cursor.fetchall()
    #     return result['植物数量'] if result else 0
#属
class GenusDAO(BaseDAO):
    def insert_genus(self, genus):
        query = "INSERT INTO 属 (属ID, 属名) VALUES (?, ?)"
        values = (genus.genus_id, genus.genus_name)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_genus_by_name(self, genus_name):
        query = "SELECT * FROM 属 WHERE 属名 = ?"
        self.cursor.execute(query, (genus_name,))
        row = self.cursor.fetchone()
        if row:
            return Genus(row[0], row[1])
        return None


#种
class SpeciesDAO(BaseDAO):
    #添加种信息
    def insert_species(self, species):
        query = "INSERT INTO 种 (种ID, 别名, 种名, 形态特征, 栽培要点,生长环境, 应用价值) VALUES (%d, %s, %s, %s, %s, %s, %s)"
        values = (species.species_id, species.alias, species.species_name, species.characteristics, species.cultivation, species.environment,  species.value)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_counties_by_species_name(self, species_name):
        query = '''
        SELECT 县.县名, 县.县ID
        FROM 种
        JOIN 县分布 ON 种.种ID = 县分布.种ID
        JOIN 县 ON 县分布.县ID = 县.县ID
        WHERE 种.种名 = %s
        '''
        self.cursor.execute(query, (species_name,))
        rows = self.cursor.fetchall()
        if not rows:
            print("未找到与该种名匹配的县信息。")
            return []
        return [County(row['县ID'], row['县名']) for row in rows]

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

    #根据种名或者别名来查询信息
    def get_species_info_by_name_or_alias(self, name_or_alias):
        query = '''
            SELECT 种ID, 别名, 种名, 形态特征,  栽培要点,生长环境,应用价值
            FROM 种
            WHERE 种名 = %s OR 别名 = %s
        '''
        self.cursor.execute(query, (name_or_alias, name_or_alias))
        row = self.cursor.fetchone()
        if row:
            return {
                '编号':row['种ID'],
                '别名':row['别名'],
                '种名':row['种名'],
                '形态特征': row['形态特征'],
                '栽培要点': row['栽培要点'],
                '生长环境': row['生长环境'],
                '应用价值': row['应用价值'],
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
        query = "UPDATE 种 SET 别名 = %s,种名 = %s,形态特征 = %s, 栽培要点 = %s, 生长环境 = %s, 应用价值 = %s  WHERE 种ID = %s"
        values = (species.alias,species.species_name,species.characteristics, species.cultivation,species.environment, species.value, species.species_id)
        self.cursor.execute(query, values)
        self.connection.commit()


    #删除种信息
    def delete_species(self, species_id):
        query = "DELETE FROM 种 WHERE 种ID = %d"
        self.cursor.execute(query, (species_id,))
        self.connection.commit()


#植物信息
#通过植物名称查询所属的科、属、种
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

    #删除植物信息
    #同时删除有关配图信息
    def delete_plant_info(self, plant_name):
        query = '''
            DELETE FROM [植物信息]
            WHERE [植物名称] = %s
        '''
        self.cursor.execute(query, (plant_name,))
        self.connection.commit()





# 类似地，为省、市、县及其分布实现DAO类
def main():
    species_dao = SpeciesDAO()
    plant_dao = plantDAO()
    picture_dao = PictureDAO()
    family_dao = FamilyDAO()

    # 测试用例：查找种名为"杜鹃"的植物所在的省、市、县
    # locations = species_dao.get_locations_by_species_name("二色补血草")
    # for province, city, county in locations:
    #     print(f"省：{province}, 市：{city}, 县：{county}")

    # shu = plant_dao.get_shu_by_plant_name("二色补血草")
    # print(f"属名:{shu}")

    # zhong = plant_dao.get_zhong_by_plant_name("二色补血草")
    # print(f"种名:{zhong}")

    # ke = plant_dao.get_ke_by_plant_name("二色补血草")
    # print(f"科名:{ke}")

    # picture_route = picture_dao.get_picture_route("二色补血草")
    # print(f"路径:{picture_route}")
    # picture_people = picture_dao.get_picture_people("二色补血草")
    # print(f"拍摄人:{picture_people}")

    # updated_species = Species(
    #     species_id=1,  # 你需要根据具体情况提供要更新的种的ID
    #     characteristics="新的形态特征",
    #     environment="新的生长环境",
    #     diseases="新的病名",
    #     alias="新的别名",
    #     value="新的应用价值",
    #     cultivation="新的栽培要点",
    #     species_name="222"
    # )

    # species_dao.update_species(updated_species)
    # environment = "阳光"
    # species_names = species_dao.get_species_names_by_environment_fuzzy(environment)

    # if species_names:
    #     print(f"根据生长环境 '{environment}' 模糊查询的种名：")
    #     for species_name in species_names:
    #         print(species_name)

    # new_family = Family(family_id='15', family_name='New Family')
    # family_dao.insert_family(new_family)

    # # 查询插入的科
    # inserted_family = family_dao.get_family_by_name('New Family')
    # if inserted_family:
    #     print(f"Insert finished!")
    # else:
    #     print("Insert failed.")
    

    # new_species = Species(
    #     species_id=1002,
    #     characteristics="测试特征",
    #     species_name="测试种名",
    #     environment="测试环境",
    #     diseases="测试病名",
    #     alias="测试别名",
    #     value="测试价值",
    #     cultivation="测试栽培要点"
    # )
    # species_dao.insert_species(new_species)

    # species_info = species_dao.get_species_info_by_name_or_alias("情人花")
    # if species_info:
    #     print("通过种名查询到的信息：", species_info)
    # else:
    #     print("未找到相关信息。")
     
    # 测试用例：查询每个科名对应的植物数量
    # keming = family_dao.get_plant_count_by_family("白花丹科")
    # plant_count = family_dao.get_plant_count_by_family(keming)
    # print(f"科名: {keming}, 植物数量: {plant_count}")

    # picture_dao = PictureDAO()

    # # 假设有一个种ID为1的植物，你可以用这个种ID来测试
    # species_id_to_test = 1

    # pictures_info = picture_dao.get_all_pictures_by_species_id(species_id_to_test)

    # if pictures_info:
    #     print(f"种ID为 {species_id_to_test} 的植物的配图信息：")
    #     for info in pictures_info:
    #         print(f"配图存储路径: {info['配图存储路径']}")
    #         print(f"配图拍摄人: {info['配图拍摄人']}")
    #         print(f"配图拍摄地点: {info['配图拍摄地点']}")
    #         print(f"配图描述: {info['配图描述']}")
    #         print("\n")
    # else:
    #     print(f"没有找到种ID为 {species_id_to_test} 的植物的配图信息。")

    # updated_species = Species(
    #     species_id=8,
    #     species_name = "新种名",
    #     alias="新别名",
    #     characteristics="新形态特征",
    #     cultivation="新栽培要点",
    #     environment="新生长环境",
    #     value="新应用价值"
    # )

    # # 更新种信息
    # species_dao = SpeciesDAO()
    # species_dao.update_species(updated_species)

    # # 指定要删除的种的ID
    # species_id_to_delete = 123

    # # 使用 SpeciesDAO 删除指定ID的种信息
    # species_dao = SpeciesDAO()
    # species_dao.delete_species(species_id_to_delete)

    # # 打印成功信息
    # print(f"ID为 {species_id_to_delete} 的种信息已从数据库中删除。")


if __name__ == "__main__":
    main()


