"""Class to create a python Layer object from JSON.


Copyright 2013 Google Inc.

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""
import gme_datasource


class Layer(object):
  """Google Maps Engine Layer.

  Properties are documented at
  https://developers.google.com/maps-engine/documentation/reference/v1/
  """

  def __init__(self, id=None, name=None, description=None,
               bbox=None, datasourceType=None, datasources=None, **kwargs):
    self.id = id
    self.name = name
    self.description = description
    self.bbox = bbox
    self.datasourceType = datasourceType
    if datasources:
      self.dataSources = [
          gme_datasource.DataSource(**x) for x in datasources]
    else:
      self.dataSources = []
