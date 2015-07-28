__author__ = 'janomar'
from airflow.operators.jdbc_operator import JdbcOperator
from airflow.utils import apply_defaults
from datetime import timedelta


class ExasolOperator(JdbcOperator):
    """
    Alias for backwards compatibility
    """
    @apply_defaults
    def __init__(self, retries=35, retry_delay=timedelta(seconds=300), exasol_conn_id='exasol_default', *args, **kwargs):
        super(ExasolOperator,self).__init__(retries=retries, retry_delay=retry_delay, jdbc_conn_id=exasol_conn_id, *args,**kwargs)

     # Don't use get_records for now. We may have to investigate our options if we need output from executing
     # scripts in exasol again.
     #
     #
     # get_records should be side effect free, right now that's not the case... it shouldn't require any kind of commit
     # fix autocommit somehow, if we have to use get_records - try to avoid exasol specific hook if possible..
     #def execute(self, context):
     #    logging.info('Executing: ' + self.sql)
     #    self.hook = JdbcHook(jdbc_conn_id=self.jdbc_conn_id)
     #    for row in self.hook.get_records(self.sql, self.autocommit):
     #        logging.info('Result: ' + ','.join(map(str,row)) )