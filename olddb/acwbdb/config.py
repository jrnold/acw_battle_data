# import sys
# from os import path
# import codecs

# import sqlalchemy as sa
# import yaml

# from acwbdb import model

# class Config(object):
#     """ Configuration """

#     def load(self, configfile='conf.yaml'):
#         """ Initialize Conf from yaml file

#         Parameters
#         -------------
#         configfile: Unicode
#            Path to yaml configuration file

#         """
#         with codecs.open(configfile, 'r', encoding='utf8') as f:
#             conf = yaml.load(f)
#         for k, v in conf.iteritems():
#             setattr(self, k, v)
#         self._normalize_paths(path.abspath(path.dirname(configfile)))

#     def _normalize_paths(self, dir):
#         for k, v in self.paths.iteritems():
#             self.paths[k] = v if path.isabs(v) else path.normpath(path.join(dir, v))

#     def bind(self):
#         """Bind database instance"""
#         model.Base.metadata.bind = sa.create_engine(self.database['engine'],
#                                                     **self.database['kwargs'])

# CONFIG = Config()

