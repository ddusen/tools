#!/bin/sh

#获取yqj全量数据
getFullDoseDB(){
    echo '-----START -----'
    
    timestamp=`date +%s`
    echo $timestamp
    randomInt=`${timestamp}:0-2:5`
    echo $randomInt
    requestUrl='https://cdb.api.qcloud.com/v2/index.php?
		Action=DescribeCdbInstances
		&SecretId=your_secret_id
		&Region=ap-guangzhou
		&Timestamp='${timestamp}'
		&Nonce='${randomInt}'
		&Signature=mysignature
		&SignatureMethod=HmacSHA256'
	echo $requestUrl
    echo '-----END.-----'
}

getFullDoseDB