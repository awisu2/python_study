from object_property_helper import set_property, set_property_decorator

class Base(object):
  # 普通に記述するとパブリックアクセス可能なプロパティ
  pubname = ''

  # "__"をつけるとプライベート
  __name = ''

  x = None

  @classmethod
  def create(cls, name):
    return cls(name)

  @staticmethod
  def any_consts():
    return ('a', 'b', 'c')

  @set_property_decorator('y', 123, is_read=True)
  def __init__(self, name):
    """
    constructor
    """
    print(f'check property already set: {self.__name}, {self.pubname}')

    self.__name = name
    # テストのため、pub_をつけてセット
    self.pubname = 'pub_' + name

    set_property(self, 'x', 999)

  # いわゆるgetter
  @property
  def name(self):
    return self.__name

  # いわゆるsetter
  @name.setter
  def name(self, name):
    self.__name = name

class Sub(Base):
  def __init__(self, subname, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.__subname = subname

  @property
  def subname(self):
    return self.__subname

class SubNoInit(Base):
  pass

