import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import psycopg2

c = 1

DSN = 'postgresql://postgres:qwr1d@localhost:5432/postgres'  # адрес базы
engine = sqlalchemy.create_engine(DSN)  # создаем движок

conn = psycopg2.connect(database='postgres', user='postgres', password='qwr1d')

Session = sessionmaker(bind=engine)


def drop_table():
    with conn.cursor() as cur:
        cur.execute('''
                            drop table data_user;

                        '''
                    )
    conn.commit()
    print('удалена таблица data_user')


def create_table():
    with conn.cursor() as cur:
        # cur.execute('''
        #     drop table data_user;
        #
        # '''
        # )

        cur.execute('''
                create table if not exists data_user(
                    id serial primary key,
                    id_user int,
                    foto_url varchar(250) unique

                    );
            '''
                    )
        conn.commit()
        print('создана таблица data_user')


def save_tabel_data_user(data):
    with conn.cursor() as cur:
        cur.execute('''
                              insert into data_user(id_user,foto_url)
                              values(%s,%s); 

                          ''', (data[0], data[4]))
        conn.commit()
        print('данные внесены')


list = [3028643, 420813254, 420813254, 2964356, 1]
l = [[3028643,'g','h',89],[492437291, 'Beautiful', 'Lady', 34974, 'https://sun9-32.userapi.com/impf/c850736/v850736728/1bc776/qdEYVBbjizc.jpg?size=104x130&quality=96&sign=2a7511c566a0dd2345941e50ef39f0d0&c_uniq_tag=lfbeSzKgDgl0Sc1qk-TwabUzG0xbL3tDrpd7d5llvTw&type=album'],[420813254,'A','A',77], [201202594, 'Полина', 'Артамонова', 5339, 'https://sun9-79.userapi.com/impg/pc8X5OFJfnk6L9pvTQVj5kAaaIY8B4k-q_kLdw/eO7BFhY_3oM.jpg?size=115x130&quality=96&sign=dd877f00b94281f51bd1736fb2b77dfb&c_uniq_tag=DPsYcHriLXbgymI_Yb7kxpmy7QrNDuyUT-QLmRyZ78c&type=album'], [251569384, 'Настасья', 'Рыжова', 2699, 'https://sun9-30.userapi.com/impg/UitPBegvGLwW-1ePdp4k04Ohvxt_8P1ORApJDw/QbA_rDMHsv4.jpg?size=97x130&quality=96&sign=00c487e808a6bde5f8dfe884b606193a&c_uniq_tag=dSM2BNImi3iuE7pYmOPQFtt4VmWw-oml7GPGJfyBYgI&type=album'], [397542585, 'Маришка', 'Емельянова', 2153, 'https://sun9-4.userapi.com/impg/5ntGLQb0-hhl89LvsrRRo8gzsfnu_0pNEcnYeQ/oJSawN1X1p8.jpg?size=62x75&quality=95&sign=5a63401baab7b8d115e217b0e4a61f89&c_uniq_tag=tPbcMBc-_A-U9a28fsXfmotTs4eNFiGCZ9dIjJPIE8E&type=album'], [420823235, 'Виктория', 'Прямая', 1426, 'https://sun1-17.userapi.com/impf/c836432/v836432235/31329/lJrP4VWgfMs.jpg?size=77x130&quality=96&sign=e4605514db7789ab6b161fb856b5724b&c_uniq_tag=pWcN2iwxMwK88LZtdq5y5ZQvcHXtGxqMwnEBu2aYRrc&type=album'], [21381919, 'Юлия', 'Старостина', 1329, 'https://sun1-87.userapi.com/impg/mBreduDV4Dnd9SmweumHdJz-ufvBtzb42F-Cgw/KbwKOJmyaZ8.jpg?size=56x75&quality=95&sign=2c70a434d05c4dd41e26427c9179dcf0&c_uniq_tag=Z6ZDQishwAxlzFvl_2dPlUTsHxhEz53S5e-ZU_zAUOo&type=album'], [12036549, 'Светлана', 'Дорофеева', 1092, 'https://sun1-93.userapi.com/impf/uUePLEtB_J1jwCqf0L04BQSoSlGZYyn1EtlD4g/LO1gEbAcyzY.jpg?size=107x130&quality=96&sign=1d04d6f2b3e936af43c28273181e1453&c_uniq_tag=nO6L9dVpQNN8nKoXPKEwelZ223UqPF-7v0SoU_7jalo&type=album'], [493632707, 'Светлана', 'Шестакова', 940, 'https://sun1-28.userapi.com/impg/_MlRTCYEXEuubEwHTFwMBDMND6qeVYtXQC1aEg/2wwo68AeLAw.jpg?size=130x97&quality=96&sign=c95ea3d2af556275cf14e6ef26c5bc93&c_uniq_tag=y8LXlzC-iTff4gEuTe23rwfxxu4CH0B2V_aj-zXIR9k&type=album'], [226933718, 'Кристина', 'Пономарёва', 927, 'https://sun9-63.userapi.com/impf/MuEPMqklB2a2XbSjjo2OM3DwYXU3uMsk8LNZDg/f7Fhj7u3aj8.jpg?size=130x130&quality=96&sign=9837f9f68af214be7baea12ae4d0b226&c_uniq_tag=Nvmb1T_PvvRMLdyLsUdY4WzMbPfOxH1WzAtpEZIow0w&type=album'], [55241865, 'Мария', 'Кадиева', 753, 'https://sun1-84.userapi.com/impg/tBvb0pleDyQdyEummYzPpv2wZPsTemyEeZ0x0g/IqumM4mX6rY.jpg?size=56x75&quality=95&sign=27880b07ddc5b88bc2a8975ada1c47f1&c_uniq_tag=QPYFeMXvfLZn6QeAT2IQ47EyFaxTAiq7huh-ie8z3_Q&type=album'], [62786550, 'Ольга', 'Царькова', 513, 'https://sun9-19.userapi.com/impf/c840539/v840539430/5c53b/6SmF_OjYfyc.jpg?size=130x130&quality=96&sign=70ef48dc052b619ebc55dfde4c95aff3&c_uniq_tag=-K_bXaPqDefSmD5De6WHbKTdMT9WvP8tsTkYbb4pJeU&type=album'], [441264119, 'Рита', 'Добромирова', 441, 'https://sun9-22.userapi.com/impg/c855420/v855420409/206f94/5hiOBMna9Iw.jpg?size=130x130&quality=96&sign=461efba3cf0b4a1980f13e32da6fdafc&c_uniq_tag=SV78Bw7qU-hUXlxUPvXwj-YTEt50-KFadyLjXhVoGLk&type=album'], [53953300, 'Елена', 'Костыря', 439, 'https://sun1-21.userapi.com/impf/c626824/v626824300/3558/b3QvPKVMrks.jpg?size=97x130&quality=96&sign=020d63dbd2cb24f2e2cf7ef64abca644&c_uniq_tag=QLIl1ApLKgkrcFTopQUax0CV5vC6QuxdrBDFkWPegr0&type=album'], [545441213, 'Варвара', 'Измайлова', 307, 'https://sun1-88.userapi.com/impg/I3-niFx8JArHNhacBWoDqiO7eCCcv0a4q2RjfQ/hotnDWT8xao.jpg?size=60x75&quality=95&sign=e4e91c6bd35001ae6fbefac6f93c736d&c_uniq_tag=rvA2PCkpKbGdScwvwSGwtlZO6h5DCWIsyYzuqhwULHA&type=album'], [293362733, 'Оксана', 'Юзепчук', 119, 'https://sun1-87.userapi.com/impg/c855132/v855132170/2101f1/4dcTkSfJdfs.jpg?size=104x130&quality=96&sign=6d036863f054c83a244633a6a7862679&c_uniq_tag=I15S8rzLiwZU0zOMzlAzAYpII7B0NwxqMJrCxX-42qs&type=album'], [558444531, 'Васелиса', 'Васина', 86, 'https://sun1-20.userapi.com/impf/c854024/v854024939/166880/YZUlanI0i9o.jpg?size=97x130&quality=96&sign=8253adcd23ea51cc2cd1e17f2733533c&c_uniq_tag=0XPMXhM2iCoILVsK0Bbwa8uc76TiEAGdHnIYjqBt2s4&type=album'], [372628892, 'Саби', 'Магомедова', 71, 'https://sun9-25.userapi.com/impg/c857124/v857124057/12488d/bJkke4vkfDw.jpg?size=86x130&quality=96&sign=1971343d8cd0e38394055bbd3ca60ff1&c_uniq_tag=zSYzZjCh7WEuSz520lAiG6pudMjRCfVBFFQGWu4Gow4&type=album'], [375021230, 'Наталия', 'Панферова', 67, 'https://sun9-61.userapi.com/impf/c637324/v637324230/8ecd/5l_xWttxeUc.jpg?size=97x130&quality=96&sign=ca174fe1540962be7c5180a85ec62ecb&c_uniq_tag=OrAWla2Ndeibb2aGoi_BJs6iKxnONNHsBqSRN3c4pzk&type=album']]


def send_db(id):
    a = str(id)
    with conn.cursor() as cur:
        cur.execute('''
                select id from data_user where id_user = %s;
            ''', (a,))
        a = cur.fetchone()
        # if a == None:
        #     print(a)
        #     return a
        # else:
        #     print('no',a)
        return a


# def preza(short_list):
#     print('NO', short_list)
#
#
# def create_list_for_prezentation(list):
#     print(list)
#     list_for_prezenatation = []
#     for i in list:
#         a = send_db(i[0])
#         if a == None:
#             list_for_prezenatation.append(i)
#             if len(list_for_prezenatation) == 3:
#                 preza(list_for_prezenatation)
#                 list1 = list.pop(0)
#         else:
#             print('есть в базе', i)
#     print(list1, list)
#     # for i in list:
#     #     a = send_db(i[0])
#     #     if a == None:
#     #         preza(i)
#     #     else:
#     #         print('есть в базе',list)


# save_tabel_data_user(201202594,34)
# create_list_for_prezentation(l)
# with conn.cursor() as cur:
#     cur.execute('''
#             select id from data_user where id_user = %s;
#         ''', ('3028643',))
#     a = cur.fetchone()
#     print(a)
# for i in list:
#     send_db(i)
# if a == None:
#     print('yyyoho',i)
# send_db(3028643)

# drop_table()
# create_table()
# li = list_for_presentation(a2)
# print('ist for present - ',len(li),li)