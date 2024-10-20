#!/bin/bash
echo $(whoami)
export PYSPARK_DRIVER_PYTHON=python
export PYSPARK_PYTHON=python
export TZ=PST
TIMESTAMP="$(date '+%Y%m%d%H%M%S')"
# making dir if not exist
mkdir -p /app/logs
gen_file_anonymiz_data_log="/app/logs/gen_anonymiz_data_log.txt"
success_or_failure="/app/logs/success_or_failure.log"

if [ -e $success_or_failure ]
then
cat /dev/null > $success_or_failure
fi


export BASEDIR=/app
cd $BASEDIR
echo "$(date '+%Y-%m-%d %H:%M:%S')-----start anonymize process"
_all_jobs() {
    # ---------------------------------------------------------------------------------------------------------------
    # Generate Key
    # ---------------------------------------------------------------------------------------------------------------
    "_gen_key"                                                                                               \
    # ---------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------------------
    # Generate Encrypt Data
    # ---------------------------------------------------------------------------------------------------------------
    "_gen_encrypt_data"                                                                                            \
    # ---------------------------------------------------------------------------------------------------------------
    # Generate Encrypt Data
    # ---------------------------------------------------------------------------------------------------------------
    "_gen_decrypt_data"                                                                                            \
    # ----
    }
_gen_key() {
  echo "$(date '+%Y-%m-%d %H:%M:%S') start gen_key generate_key.py"
  spark-submit --master local[1] --driver-memory 1G --executor-memory 1G --executor-cores 1  --num-executors 1  generate_key.py > $gen_file_anonymiz_data_log 2>&1
  retcode=`echo $?`
  case "$retcode" in
  0) echo "$(date '+%Y-%m-%d %H:%M:%S')-----generate_key generate_key.py execution successful" ;;
  1) echo "$(date '+%Y-%m-%d %H:%M:%S')-----generate_key generate_key.py exit with failure" ;;
  2) echo "$(date '+%Y-%m-%d %H:%M:%S')-----generate_key generate_key.py exit with warning" ;;
  *) echo "$(date '+%Y-%m-%d %H:%M:%S')-----generate_key generate_key.pyUnknow return code" ;;
  esac
  if [ $retcode -ne 0 ]
  then
  echo "$(date '+%Y-%m-%d %H:%M:%S')-----generate_key generate_key.py with failure code: $retcode, investigate logs, code and then restart"
  echo "$timestamp generate_key failure " >> $success_or_failure
  exit $retcode
  else
  echo "$(date '+%Y-%m-%d %H:%M:%S')-----generate_key generate_key.py with success code: $retcode "
  echo "$timestamp generate_key success " >> $success_or_failure
  fi
}
_gen_encrypt_data() {
  echo "$(date '+%Y-%m-%d %H:%M:%S') start encrypt_data  encrypt_data.py"
  spark-submit --master local[1] --driver-memory 1G --executor-memory 1G --executor-cores 1  --num-executors 1  encrypt_data.py > $gen_file_anonymiz_data_log 2>&1
  retcode=`echo $?`
  case "$retcode" in
  0) echo "$(date '+%Y-%m-%d %H:%M:%S')-----encrypt_data encrypt_data.py execution successful" ;;
  1) echo "$(date '+%Y-%m-%d %H:%M:%S')-----encrypt_data encrypt_data.py exit with failure" ;;
  2) echo "$(date '+%Y-%m-%d %H:%M:%S')-----encrypt_data encrypt_data.py exit with warning" ;;
  *) echo "$(date '+%Y-%m-%d %H:%M:%S')-----encrypt_data encrypt_data.py Unknow return code" ;;
  esac
  if [ $retcode -ne 0 ]
  then
  echo "$(date '+%Y-%m-%d %H:%M:%S')-----encrypt_data encrypt_data.py with failure code: $retcode, investigate logs, code and then restart"
  echo "$timestamp encrypt_data failure " >> $success_or_failure
  exit $retcode
  else
  echo "$(date '+%Y-%m-%d %H:%M:%S')-----encrypt_data encrypt_data.py with success code: $retcode "
  echo "$timestamp encrypt_data success " >> $success_or_failure
  fi
}
_gen_decrypt_data() {
  echo "$(date '+%Y-%m-%d %H:%M:%S') start decrypt_data  decrypt_data.py"
  spark-submit --master local[1] --driver-memory 1G --executor-memory 1G --executor-cores 1  --num-executors 1  decrypt_data.py > $gen_file_anonymiz_data_log 2>&1
  retcode=`echo $?`
  case "$retcode" in
  0) echo "$(date '+%Y-%m-%d %H:%M:%S')-----decrypt_data decrypt_data.py execution successful" ;;
  1) echo "$(date '+%Y-%m-%d %H:%M:%S')-----decrypt_data decrypt_data.py exit with failure" ;;
  2) echo "$(date '+%Y-%m-%d %H:%M:%S')-----decrypt_data decrypt_data.py exit with warning" ;;
  *) echo "$(date '+%Y-%m-%d %H:%M:%S')-----decrypt_data decrypt_data.py Unknow return code" ;;
  esac
  if [ $retcode -ne 0 ]
  then
  echo "$(date '+%Y-%m-%d %H:%M:%S')-----decrypt_data decrypt_data.py with failure code: $retcode, investigate logs, code and then restart"
  echo "$timestamp decrypt_data failure " >> $success_or_failure
  exit $retcode
  else
  echo "$(date '+%Y-%m-%d %H:%M:%S')-----decrypt_data decrypt_data.py with success code: $retcode "
  echo "$timestamp decrypt_data success " >> $success_or_failure
  fi
}
_all_jobs
echo "$(date '+%Y-%m-%d %H:%M:%S')-----end anonymize process"