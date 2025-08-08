#
# Python Imaris Library to initiate communication with Imaris via ImarisXT
#
# Copyright by Bitplane AG
#

import sys, os
vPrivatePath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'private')
if not os.path.exists(vPrivatePath):
  print('Private resource directory not available. The directory \'private\' can be found in \'XT/python\' in the Imaris Installation.')
sys.path.append(vPrivatePath)

import IceClient

import Imaris

import time

class ImarisLib:

  _mIceClient = None
  _mEndPoints = 'default -p 4029'
  _mServerTimeoutMillisec = 10000

  def __GetIceClient(self):
    if self._mIceClient is None:
      self._mIceClient = IceClient.IceClient('ImarisServer', self._mEndPoints, self._mServerTimeoutMillisec)
    return self._mIceClient


  def Disconnect(self):
    time.sleep(2)
    if self._mIceClient is not None:
      self._mIceClient.Terminate()
      self._mIceClient = None


  def SetEndPoints(self, aEndPoints):
    self.Disconnect()
    self._mEndPoints = aEndPoints


  def GetServer(self):
    try:
      return self.__GetIceClient().GetServer()
    except:
      self.Disconnect()
      return None


  def GetApplication(self, aImarisId):
    try:
      vServer = self.GetServer()
      if vServer is None:
        raise
      vImarisApplicationObjectProxy = vServer.GetObject(aImarisId)
      vImaris = Imaris.IApplicationPrx.checkedCast(vImarisApplicationObjectProxy)
      return vImaris
    except:
      print('Could not connect to Imaris and initialize its python object!')
      self.Disconnect()
      return None
