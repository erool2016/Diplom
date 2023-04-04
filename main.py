from random import randrange

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

import Data_Base

from operator import itemgetter




def get_token():
    with open('tok111.txt', 'r') as f:
        return f.readline()

def get_servis_key():
    with open('token_vkinder_servis_key.txt', 'r') as f:
        return f.readline()
vk = vk_api.VkApi(token=get_servis_key())
vk2 = vk_api.VkApi(token=get_token())
longpoll = VkLongPoll(vk)

user_id = 0
data_user_for_find = {} #словарь с данными для поиска id , sity, sex
def write_msg(user_id, message,attachment=None):
    vk.method('messages.send', {'user_id': user_id, 'message': message,  'random_id': randrange(10 ** 7),'attachment':attachment})

def session_longpoll():
    '''получаем ответ в чате бота'''
    session = vk_api.VkApi(get_servis_key())
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            # text = event.text.lower()
            user_id = event.user_id
            write_msg(user_id, f"Хай, {event.user_id}")
            request_user  = event.text.lower()

            #print('requests users - ', request_user)

            return request_user,user_id


def get_profile_user(user_id):
    '''получаем информацию о пользователе и заносим в словарь, возвращаем словарь'''

    req = vk2.method('users.get',
                         {
                             'user_id': user_id,
                             'fields': 'bdate,city,sex,photo_id,about'
                         }
                         )


    data_user_for_find['bdate']=req[0]['bdate']
    data_user_for_find['city'] = req[0]['city']['id']
    data_user_for_find['sex'] = req[0]['sex']
    # print('data for find',data_user_for_find)
    return data_user_for_find

def change_sex(data_user_ff):
    if data_user_ff['sex'] == 1:
        data_user_for_find['sex'] = 2
        return data_user_for_find
    else:
        data_user_for_find['sex'] = 1
        return data_user_for_find

def get_user_foto(i):
    '''Принимает список айди  возвращает список списков [ количество лайков,самых популярных id] '''
    list = []
    # print(i, '----')
    session = vk_api.VkApi(token=get_token())
    response = session.method('photos.get', {
        'owner_id': i,
        'album_id': 'profile',
        'extended': 1,
        'photo_sizes': 1})
    a = response['items']
    # print('user',i)
    # pprint(a)
    for item in a:
        # print(item['likes']['count'])
        # print(item['sizes'][0]['url'])
        list.append(item['likes']['count'])
        url = item['sizes'][0]['url']
    # print(list)
    return list,url

def presentation(list,user_id):
    # print('list sorted for presentation',list)
    n=0
    while n < 3:
        # print(list[n])
        write_msg(user_id,f'{list[n][1]},{list[n][2]},{list[n][3]}',attachment=list[n][4])
        n+=1

    # while n < 3:
    #     write_msg(user_id,f'{list[1]},{list[2]}',list[4])
    #     n+=1

def what_to_do(user_id,list):
    print(user_id,list)
    write_msg(user_id,'Что будем делать далее ( w - смотреть далее / другая кнопка - новый поиск)',attachment=None)
    answer, user_id = session_longpoll()
    if answer == 'w':
        print(answer)
        create_list_for_prezentation(list,user_id)
    if answer != 'w':
        print(answer)
        start()


def save_db(lists,user_id,list_for_view):
    print('list for save',lists)
    for list in lists:
        Data_Base.save_tabel_data_user(list)
    what_to_do(user_id,list_for_view)


def create_list_for_prezentation(list,user_id):
    # print(list)
    list_for_prezenatation = []
    for i in list:
        a = Data_Base.send_db(i[0])
        if a == None:
            list_for_prezenatation.append(i)
            if len(list_for_prezenatation) == 3:
                presentation(list_for_prezenatation,user_id)
                list1 = list.pop(0)
                # print('data from DB',list1)
                # Data_Base.save_tabel_data_user(list1)
                save_db(list_for_prezenatation,user_id,list)
        else:
            print('есть в базе', i)

def sorted_list(list,user_id):
    # print(list)
    list = (sorted(list, key=itemgetter(3), reverse=True))
    print('отсортированный список',list)
    create_list_for_prezentation(list,user_id)


def get_foto_likes_list(list,user_id):
    '''получаем список с ай ди, имя,фамилия и получаем лайки с фото'''
    # print('list for foto get',list)
    for items in list:
        lists, url = get_user_foto(items[0])
        items.append(sum(lists))
        items.append(url)
    # print('не отсортированный список',list)
    sorted_list(list,user_id)




def creating_a_list(resp,user_id):
    # print('---',resp)
    result = []

    for i in resp:
        r = []
        if i['is_closed'] == False:
            r.append(i['id'])
            r.append(i['first_name'])
            r.append(i['last_name'])

            result.append(r)
    # print(result)
    get_foto_likes_list(result,user_id)

def find_users(data_user_for_find,user_id):
    n = data_user_for_find['bdate'].split('.')
    # print('data for find canged sex',data_user_for_find)
    resp = vk2.method('users.search', {
        #'age_from' : int(n[2]) - 3,
        'age_to' : int(n[2]) + 3,
        'sex': data_user_for_find['sex'],
        'city': data_user_for_find['city'],
        'fields': 'bdate,sex,photo_id,about,city,relation,inerests,domain',
        'status': 6,
        'count': 25,
        'has_photo': 1,
        'v': 5.131
    })
    # pprint(resp)
    creating_a_list(resp['items'],user_id)

def start_find(user_id):
    '''начало поиска'''
    # print('start find',user_id)
    # print('инфа для поиска',get_profile_user(user_id))
    # Data_Base.create_table()
    get_profile_user(user_id)
    change_sex(data_user_for_find)
    find_users(data_user_for_find,user_id)

def start():
    '''начало'''
    requests_longpoll, user_id = session_longpoll()
    print('-----', requests_longpoll,user_id)
    if requests_longpoll == 'q':
        print('q')
        start_find(user_id)
    elif requests_longpoll == 'more':
        start()
    else:
        print('пока')

        return


if __name__ == '__main__':
    # Data_Base.drop_table()
    Data_Base.create_table()
    start()

