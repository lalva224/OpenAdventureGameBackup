import axios from 'axios'

export const api = axios.create({
baseURL :'https://openadventure.duckdns.org:8000/api/v1/adventuregame/',

})