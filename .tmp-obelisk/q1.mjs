const s = sessions({ project: '%tim-professional%', limit: 40 });
return s.map(x => ({ id: x.id, title: (x.title||'').slice(0,90), src: x.source, started: x.started_at, msgs: x.message_count, cwd: (x.cwd||'').slice(-40) }));
