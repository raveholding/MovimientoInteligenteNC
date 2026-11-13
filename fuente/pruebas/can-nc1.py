from playwright.sync_api import sync_playwright
res=[]
def chk(c,m):print(('OK   ' if c else 'FALLA ')+m);res.append(bool(c))
with sync_playwright() as p:
    b=p.chromium.launch(args=['--no-proxy-server']);pg=b.new_page(viewport={'width':1300,'height':900});ev=pg.evaluate;errs=[];pg.on('pageerror',lambda e:errs.append(str(e)[:300]))
    pg.goto('file:///tmp/rave/nc.html#acceso');pg.wait_for_timeout(1500);pg.select_option('#lu',index=0);pg.fill('#lp','1234');pg.click('[data-act=login]');pg.wait_for_timeout(800)
    ev("crmTab='canales';go('crm')");pg.wait_for_timeout(500)
    chk(pg.locator('.can-card').count()==8,'8 canales en Atención al cliente')
    pg.click('[data-act=canTodo]');pg.wait_for_timeout(500);ev("$$('#modal-root .ov').forEach(o=>o.remove())")
    st=ev("Object.fromEntries(CANAL_L.map(k=>[k,canEstado(k)]))");chk(st['web']=='api' and pg.locator('.can-card').count()==8,'conectar todo con un clic (sin WhatsApp ni redes cargadas: avisa qué falta) %s'%st)
    pg.screenshot(path='/tmp/rave/nc1.png')
    ev("rerender()");pg.wait_for_timeout(300);pg.click('.can-card [data-act=canAbrir][data-k=tg]');pg.wait_for_timeout(300);pg.fill('#cn-v','@MovInteligente');pg.click('.ov [data-m=ok]');pg.wait_for_timeout(300)
    chk(ev("canLink('tg')")=='https://t.me/MovInteligente','Telegram en un paso')
    chk(any(x['k']=='tg' for x in ev("RAVE_API.site().canales")),'se publica para los socios')
    ev("(()=>{const c=crmNew({chan:'tg',name:'Socio'});crmAdd(c,'in','Hola');window.__op=[];window.open=u=>{window.__op.push(u);return null};crmSend(c,'Hola!');})()");pg.wait_for_timeout(300)
    chk(any('telegram' in (u or '') for u in ev("window.__op")),'responder por Telegram abre la app con el texto copiado')
    chk(not errs,'sin errores JS '+str(errs[:3]))
    b.close()
print('%d/%d'%(sum(res),len(res)))
