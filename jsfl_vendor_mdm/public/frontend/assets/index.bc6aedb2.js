var h=(n,o,t)=>new Promise((r,e)=>{var s=a=>{try{l(t.next(a))}catch(p){e(p)}},c=a=>{try{l(t.throw(a))}catch(p){e(p)}},l=a=>a.done?r(a.value):Promise.resolve(a.value).then(s,c);l((t=t.apply(n,o)).next())});import{c as _,r as L,a as v,b as y,d as P,_ as I,e as R,o as A,f as O,g as j,h as C,s as b,i as D,j as V,C as k,I as T,k as w}from"./vendor.2391a1cf.js";const S=function(){const o=document.createElement("link").relList;if(o&&o.supports&&o.supports("modulepreload"))return;for(const e of document.querySelectorAll('link[rel="modulepreload"]'))r(e);new MutationObserver(e=>{for(const s of e)if(s.type==="childList")for(const c of s.addedNodes)c.tagName==="LINK"&&c.rel==="modulepreload"&&r(c)}).observe(document,{childList:!0,subtree:!0});function t(e){const s={};return e.integrity&&(s.integrity=e.integrity),e.referrerpolicy&&(s.referrerPolicy=e.referrerpolicy),e.crossorigin==="use-credentials"?s.credentials="include":e.crossorigin==="anonymous"?s.credentials="omit":s.credentials="same-origin",s}function r(e){if(e.ep)return;e.ep=!0;const s=t(e);fetch(e.href,s)}};S();const $="modulepreload",E={},H="/assets/jsfl_vendor_mdm/frontend/",i=function(o,t){return!t||t.length===0?o():Promise.all(t.map(r=>{if(r=`${H}${r}`,r in E)return;E[r]=!0;const e=r.endsWith(".css"),s=e?'[rel="stylesheet"]':"";if(document.querySelector(`link[href="${r}"]${s}`))return;const c=document.createElement("link");if(c.rel=e?"stylesheet":$,e||(c.as="script",c.crossOrigin=""),c.href=r,document.head.appendChild(c),e)return new Promise((l,a)=>{c.addEventListener("load",l),c.addEventListener("error",a)})})).then(()=>o())},f=_({url:"frappe.auth.get_logged_user",cache:"User",onError(n){n&&n.exc_type==="AuthenticationError"&&m.push({name:"LoginPage"})}});function g(){let o=new URLSearchParams(document.cookie.split("; ").join("&")).get("user_id");return o==="Guest"&&(o=null),o}const d=L({login:_({url:"login",makeParams({email:n,password:o}){return{usr:n,pwd:o}},onSuccess(n){f.reload(),d.user=g(),d.login.reset(),m.replace(n.default_route||"/codeofConduct")}}),logout:_({url:"logout",onSuccess(){f.reset(),d.user=g(),m.replace({name:"Login"})}}),user:g(),isLoggedIn:v(()=>!!d.user)}),N=[{path:"/",name:"Home",component:()=>i(()=>import("./Home.2e783468.js"),["assets/Home.2e783468.js","assets/Home.3b07efae.css","assets/vendor.2391a1cf.js","assets/vendor.f874cace.css"]),children:[{path:"/welcome",component:()=>i(()=>import("./Welcomehome.43af5676.js"),["assets/Welcomehome.43af5676.js","assets/Welcomehome.46b26f7f.css","assets/vendor.2391a1cf.js","assets/vendor.f874cace.css"])},{path:"/companydetails",component:()=>i(()=>import("./Companydetails.be8c5a0b.js"),["assets/Companydetails.be8c5a0b.js","assets/Companydetails.7e131e8b.css","assets/vendor.2391a1cf.js","assets/vendor.f874cace.css"])},{path:"/Categorybusiness",component:()=>i(()=>import("./Categorybusiness.964caca7.js"),["assets/Categorybusiness.964caca7.js","assets/Categorybusiness.8210f9bf.css","assets/vendor.2391a1cf.js","assets/vendor.f874cace.css"])},{path:"/contactdetails",component:()=>i(()=>import("./Contactdetails.c855447a.js"),["assets/Contactdetails.c855447a.js","assets/Contactdetails.0bfa676b.css","assets/vendor.2391a1cf.js","assets/vendor.f874cace.css"])},{path:"/accountdetails",component:()=>i(()=>import("./Accountdetails.09d558f6.js"),["assets/Accountdetails.09d558f6.js","assets/Accountdetails.533a477c.css","assets/vendor.2391a1cf.js","assets/vendor.f874cace.css"])},{path:"/documentdetails",component:()=>i(()=>import("./Documentdetails.6a9d6c21.js"),["assets/Documentdetails.6a9d6c21.js","assets/Documentdetails.9b8da88d.css","assets/vendor.2391a1cf.js","assets/vendor.f874cace.css"])},{path:"/codeofConduct",component:()=>i(()=>import("./codeofConduct.ed0a25cf.js"),["assets/codeofConduct.ed0a25cf.js","assets/codeofConduct.3a3360f6.css","assets/vendor.2391a1cf.js","assets/vendor.f874cace.css"])},{path:"/privacyPolicy",component:()=>i(()=>import("./privacyPolicy.fcb94431.js"),["assets/privacyPolicy.fcb94431.js","assets/privacyPolicy.b0f4ac9b.css","assets/vendor.2391a1cf.js","assets/vendor.f874cace.css"])}]},{name:"Login",path:"/account/login",component:()=>i(()=>import("./Login.a182f841.js"),["assets/Login.a182f841.js","assets/Login.654c0182.css","assets/vendor.2391a1cf.js","assets/vendor.f874cace.css"])}];let m=y({history:P("/frontend"),routes:N});m.beforeEach((n,o,t)=>h(void 0,null,function*(){let r=d.isLoggedIn;try{yield f.promise}catch(e){r=!1}n.name==="Login"&&r?t({name:"Home"}):n.name!=="Login"&&!r?t({name:"Login"}):t()}));const U={};function q(n,o){const t=R("router-view");return A(),O("div",null,[j(t)])}var x=I(U,[["render",q]]);let u=C(x);b("resourceFetcher",w);u.use(m);u.use(D);u.component("Button",V);u.component("Card",k);u.component("Input",T);u.mount("#app");export{g as a,d as s};
