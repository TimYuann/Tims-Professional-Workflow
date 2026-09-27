const sid = 'pi:01a0dd53-23d8-7568-af62-c7d6d2effdee:041e670ba84c8a4844daef972b243713d1332a019839bf247a75f324c4329901';
const rows = sql(`SELECT uuid, role, timestamp, substr(text,1,900) AS t FROM messages
 WHERE session_id=? AND role='user' AND COALESCE(is_meta,0)=0
   AND COALESCE(visibility,'visible')='visible'
 ORDER BY timestamp`, sid);
return {n: rows.length, msgs: rows};
