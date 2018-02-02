import subprocess

from operator import itemgetter

from api import call_api


def get_coldbackup():
    '''
    action: 对应接口的接口名，请参考wiki文档上对应接口的接口名
    '''
    action = 'GetCdbExportLogUrl'

    # 接口参数
    action_params = {
        'cdbInstanceId': 'cdb-ko3zdkzs',
        'type': 'coldbackup',
    }

    result = eval(bytes.decode(call_api(action, action_params)))

    result_by_date = sorted(
        result['data'], key=itemgetter('date'), reverse=True)[0]

    return result_by_date['out_url'].replace('\\', '')


def download_backup(out_url):
    command = 'rm /tmp/cdb177112_backup_yqj'
    subprocess.call(command, shell=True)

    command = 'wget -O /tmp/cdb177112_backup_yqj "{0}"'.format(out_url)
    subprocess.call(command, shell=True)


def full_restore():
    command = 'mysql -usdu -p123456 yqj -o< /tmp/cdb177112_backup_yqj'
    subprocess.call(command, shell=True)


def main():
    out_url = get_coldbackup()

    download_backup(out_url)
    full_restore()


if __name__ == '__main__':
    main()