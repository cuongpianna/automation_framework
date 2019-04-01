import sys
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from tests.config_test import get_driver

# a = get_driver()
# b = get_driver()


from base.base_requests.models import Box, ElementList, URL


class Test(Box):
    url = URL(url='https://tuoitre.vn/')
    _box_title = ElementList(name='test',
                             locator=['//*[@id="content"]/div/div[1]/div[2]/div[2]//a', 'xpath'],
                             query='''
                             select Title,SubTitle,Sapo,TypeId as TypeNewsposition,Avatar,AvatarDesc,Url,ZoneId as 
                             ZoneIdNewsposition, ObjectType ZoneIdForNews,[Order] as SortOrder,DistributionDate,
                             LastModifiedDate, CONVERT(varchar(30), NewsId) as NewsId  FROM  NewsPosition  
                             WHERE TypeId=1 AND ZoneId=0 and [Order]>0
                             ''',
                             data=[4, 'dau']
                             )
    _test = ElementList(name='test',
                        locator=['//*[@id="content"]/div/div[1]/div[2]/div[1]/div//a[not(img)]', 'xpath'],
                        query='''
                                 select Title,SubTitle,Sapo,TypeId as TypeNewsposition,Avatar,AvatarDesc,Url,ZoneId as 
                                 ZoneIdNewsposition, ObjectType ZoneIdForNews,[Order] as SortOrder,DistributionDate,
                                 LastModifiedDate, CONVERT(varchar(30), NewsId) as NewsId  FROM  NewsPosition  
                                 WHERE TypeId=1 AND ZoneId=0 and [Order]>0
                                 ''',
                        data=[4, 'dau']
                        )


# class Test2(Box):
#     url = URL(url='https://tuoitre.vn/')
#     box_title = ElementList('name', 'test')


if __name__ == '__main__':
    t = Test()
    print(t.verify_text_list_box_title())
    print(t.verify_text_list_test())
