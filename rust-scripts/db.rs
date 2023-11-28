use mysql_async;
use mysql_async::prelude::Queryable;
use mysql_async::{Row, Value, Error, Pool, Conn};

pub struct MYSQL {
    pool: Pool,
}

impl MYSQL {
    pub fn create(url: &str) -> Self {
        MYSQL {
            pool: Pool::new(url),
        }
    }

    pub async fn exec(&self, query: &str, params: Vec<Value>) -> Result<(), Error> {
        let mut conn = self.pool.get_conn().await?;
        conn.exec_drop(query, params).await?;
        Ok(())
    }

    pub async fn read(&self, query: &str, params: Vec<Value>) -> Result<Vec<Row>, Error> {
        let mut conn: Conn  = self.pool.get_conn().await?;
        let result: Vec<Row> = conn.exec(query, params).await?;

        Ok(result)
    }
}