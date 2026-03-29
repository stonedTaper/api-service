import { Client } from 'pg';
import { IParser } from '../interfaces';

class Parser implements IParser {
  async parse(query: string): Promise<any[]> {
    const client = new Client({
      host: process.env.DB_HOST,
      user: process.env.DB_USER,
      password: process.env.DB_PASSWORD,
      database: process.env.DB_NAME,
    });

    await client.connect();

    const result = await client.query(query);

    await client.end();

    return result.rows;
  }
}

export default Parser;