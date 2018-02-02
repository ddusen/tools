from QcloudApi.qcloudapi import QcloudApi

'''
module: 设置需要加载的模块
已有的模块列表：
cvm      对应   cvm.api.qcloud.com
cdb      对应   cdb.api.qcloud.com
lb       对应   lb.api.qcloud.com
trade    对应   trade.api.qcloud.com
sec      对应   csec.api.qcloud.com
image    对应   image.api.qcloud.com
monitor  对应   monitor.api.qcloud.com
cdn      对应   cdn.api.qcloud.com
'''
module = 'cdb'

'''
config: 云API的公共参数
'''
config = {
    'Region': 'ap-guangzhou',
    'secretId': 'your_secretId',
    'secretKey': 'your_secretKey',
    'method': 'GET',
    'SignatureMethod': 'HmacSHA1'
}


def call_api(action, action_params):

    try:
        service = QcloudApi(module, config)

        '''
        # 请求前可以通过下面几个方法重新设置请求的secretId/secretKey/region/method/SignatureMethod参数
        # 重新设置请求的secretId
        secretId = '你的secretId'
        service.setSecretId(secretId)
        # 重新设置请求的secretKey
        secretKey = '你的secretKey'
        service.setSecretKey(secretKey)
        # 重新设置请求的region
        region = 'ap-shanghai'
        service.setRegion(region)
        # 重新设置请求的method
        method = 'POST'
        service.setRequestMethod(method)
        # 重新设置请求的SignatureMethod
        SignatureMethod = 'HmacSHA256'
        service.setSignatureMethod(SignatureMethod)
        # 生成请求的URL，不发起请求
        print(service.generateUrl(action, action_params))
        '''

        # 调用接口，发起请求
        return service.call(action, action_params)

    except Exception as e:
        import traceback
        print('traceback.format_exc():\n%s' % traceback.format_exc())
        return None


if __name__ == '__main__':
    '''
    action: 对应接口的接口名，请参考wiki文档上对应接口的接口名
    '''
    action = 'GetCdbExportLogUrl'

    # 接口参数
    action_params = {
        'cdbInstanceId': 'cdb-ko3zdkzs',
        'type': 'coldbackup',
    }

    call_api(action, action_params)
    