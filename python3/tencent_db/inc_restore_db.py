import subprocess
import datetime

from operator import itemgetter

from api import call_api


def get_binlog():
    '''
    action: 对应接口的接口名，请参考wiki文档上对应接口的接口名
    '''
    action = 'GetCdbExportLogUrl'

    # 接口参数
    action_params = {
        'cdbInstanceId': 'cdb-ko3zdkzs',
        'type': 'binlog',
    }

    result = eval(bytes.decode(call_api(action, action_params)))

    result_by_date = sorted(
        result['data'], key=itemgetter('date'), reverse=True)[0]

    out_url = result_by_date['out_url'].replace('\\', '')
    backup_time = '{0} {1}'.format(
        result_by_date['date'].split(' ')[0], '00:00:00')
    return out_url, backup_time


def download_backup(out_url):
    command = 'rm /tmp/cdb177112_bin_mysqlbin'
    subprocess.call(command, shell=True)

    command = 'wget -O /tmp/cdb177112_bin_mysqlbin "{0}"'.format(out_url)
    subprocess.call(command, shell=True)


def increment_restore(backup_time):
    stop_time = datetime.datetime.strptime(backup_time, "%Y-%m-%d %H:%M:%S")
    start_time = stop_time + datetime.timedelta(days=-1)

    command = 'mysqlbinlog --no-defaults --start-datetime="{0}" --stop-datetime="{1}" -d yqj /tmp/cdb177112_bin_mysqlbin | mysql -uroot -p123456'.format(
        start_time, stop_time)
    subprocess.call(command, shell=True)


def main():
    result = get_binlog()

    out_url = result[0]
    backup_time = result[1]

    download_backup(out_url)
    increment_restore(backup_time)

if __name__ == '__main__':
    main()
