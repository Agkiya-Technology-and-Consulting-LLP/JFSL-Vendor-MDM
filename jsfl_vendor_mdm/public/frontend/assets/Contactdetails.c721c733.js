import{_ as c,u,r as f,t as _,c as n,e as p,o as b,f as v,l as e,x as r,y as k,z as i,A as h,g as y,w,m as g,p as N,q as V}from"./vendor.cfdf8066.js";import{a as U}from"./index.fdd41e6d.js";const M=u({name:"ContactDetails",setup(){const o=f({salutation:"",first_name:"",last_name:"",contact_number:"",email_id:"",mark_as_primary:!0,docname:"",website:"",facebook:"",linkedin:"",instagram:"",twitter:"",youtube:""}),t=U();return _(()=>{n({url:"jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.get_supplier_detail",makeParams:()=>({doc:{email:t}}),auto:!0,onSuccess:a=>{console.log(a),o.first_name=a.first_name,o.salutation=a.salutation,o.last_name=a.last_name,o.contact_number=a.contact_number,o.email_id=a.email_id,o.mark_as_primary=a.mark_as_primary,o.website=a.website,o.facebook=a.facebook,o.linkedin=a.linkedin,o.instagram=a.instagram,o.twitter=a.twitter,o.youtube=a.youtube,o.docname=a.name},onError:a=>{console.error("Error:",a)}})}),{form:o,ValidateEmail:()=>{console.log("values are here",o),n({url:"jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.save_supplier_detail",makeParams:()=>({doc:{first_name:o.first_name,salutation:o.salutation,last_name:o.last_name,email_id:o.email_id,mark_as_primary:o.mark_as_primary,docname:o.docname,website:o.website,facebook:o.facebook,linkedin:o.linkedin,instagram:o.instagram,twitter:o.twitter,youtube:o.youtube}}),auto:!0,onSuccess:a=>{console.log(a)},onError:a=>{console.error("Error:",a),alert(`An error occurred: ${a.message}`)}})}}}}),l=o=>(N("data-v-4466ce1d"),o=o(),V(),o),C={class:"container-fluid"},I={class:"row"},E={class:"col-12"},S=l(()=>e("div",{class:"bg-primary text-white p-1 rounded-top"},[e("h5",null,"Contact Details")],-1)),j={class:"row mt-3"},T={class:"col-md-4 mb-3"},$=l(()=>e("label",{for:"salutaion",class:"form-label"},"Salutation",-1)),A=l(()=>e("option",{value:"Mr"},"Mr.",-1)),B=l(()=>e("option",{value:"Mrs"},"Mrs. ",-1)),F=l(()=>e("option",{value:"Ms"},"Ms. ",-1)),L=[A,B,F],P={class:"col-md-4 mb-3"},D=l(()=>e("label",{for:"firstName",class:"form-label"},"First Name",-1)),W={class:"col-md-4 mb-3"},Y=l(()=>e("label",{for:"lastName",class:"form-label"},"Last Name",-1)),q={class:"row mt-3"},z={class:"col-md-4 mb-3"},H=l(()=>e("label",{for:"contact",class:"form-label"},"Contact Number",-1)),R={class:"col-md-4 mb-3"},G=l(()=>e("label",{for:"email",class:"form-label"},"Email ID",-1)),J={class:"col-md-4 mt-4 mb-3"},K=l(()=>e("label",{for:"markAsPrimary",class:"form-check-label"},"Mark As Primary",-1)),O=l(()=>e("div",{class:"bg-primary text-white p-1 rounded-top"},[e("h5",null,"Social Media Handlles")],-1)),Q={class:"row mt-3"},X={class:"col-md-4 mb-3"},Z=l(()=>e("label",{for:"firstName",class:"form-label"},"Website",-1)),x={class:"col-md-4 mb-3"},oo=l(()=>e("label",{for:"firstName",class:"form-label"},"Facebook",-1)),eo={class:"col-md-4 mb-3"},to=l(()=>e("label",{for:"firstName",class:"form-label"},"LinkedIn",-1)),so={class:"row mt-3"},ao={class:"col-md-4 mb-3"},lo=l(()=>e("label",{for:"firstName",class:"form-label"},"Instagram",-1)),ro={class:"col-md-4 mb-3"},io=l(()=>e("label",{for:"firstName",class:"form-label"},"Twitter",-1)),no={class:"col-md-4 mb-3"},mo=l(()=>e("label",{for:"firstName",class:"form-label"},"YouTube",-1)),co={class:"d-flex justify-content-end mt-1 mb-3"};function uo(o,t,m,a,fo,_o){const d=p("Button");return b(),v("div",C,[e("div",I,[e("div",E,[S,e("div",j,[e("div",T,[$,r(e("select",{name:"salutaion",id:"salutation",class:"form-control","onUpdate:modelValue":t[0]||(t[0]=s=>o.form.salutation=s)},L,512),[[k,o.form.salutation]])]),e("div",P,[D,r(e("input",{type:"text",class:"form-control",id:"firstName","onUpdate:modelValue":t[1]||(t[1]=s=>o.form.first_name=s),placeholder:"First Name"},null,512),[[i,o.form.first_name]])]),e("div",W,[Y,r(e("input",{type:"text",class:"form-control",id:"lastName","onUpdate:modelValue":t[2]||(t[2]=s=>o.form.last_name=s),placeholder:"Last Name"},null,512),[[i,o.form.last_name]])])]),e("div",q,[e("div",z,[H,r(e("input",{type:"tel",maxlength:"13",class:"form-control",id:"contact","onUpdate:modelValue":t[3]||(t[3]=s=>o.form.contact_number=s),placeholder:"Contact Number"},null,512),[[i,o.form.contact_number]])]),e("div",R,[G,r(e("input",{type:"email",class:"form-control",id:"email","onUpdate:modelValue":t[4]||(t[4]=s=>o.form.email_id=s),placeholder:"Email Id"},null,512),[[i,o.form.email_id]])]),e("div",J,[r(e("input",{type:"checkbox","onUpdate:modelValue":t[5]||(t[5]=s=>o.form.mark_as_primary=s),id:"markAsPrimary",class:"form-check-input mr-2"},null,512),[[h,o.form.mark_as_primary]]),K])]),O,e("div",Q,[e("div",X,[Z,r(e("input",{type:"text",class:"form-control",id:"Website","onUpdate:modelValue":t[6]||(t[6]=s=>o.form.website=s),placeholder:"Website"},null,512),[[i,o.form.website]])]),e("div",x,[oo,r(e("input",{type:"text",class:"form-control",id:"Facebook","onUpdate:modelValue":t[7]||(t[7]=s=>o.form.facebook=s),placeholder:"Facebook"},null,512),[[i,o.form.facebook]])]),e("div",eo,[to,r(e("input",{type:"text",class:"form-control",id:"LinkedIn","onUpdate:modelValue":t[8]||(t[8]=s=>o.form.linkedin=s),placeholder:"Linkedin"},null,512),[[i,o.form.linkedin]])])]),e("div",so,[e("div",ao,[lo,r(e("input",{type:"text",class:"form-control",id:"Instagram","onUpdate:modelValue":t[9]||(t[9]=s=>o.form.instagram=s),placeholder:"Instagram"},null,512),[[i,o.form.instagram]])]),e("div",ro,[io,r(e("input",{type:"text",class:"form-control",id:"Twitter","onUpdate:modelValue":t[10]||(t[10]=s=>o.form.twitter=s),placeholder:"Twitter"},null,512),[[i,o.form.twitter]])]),e("div",no,[mo,r(e("input",{type:"text",class:"form-control",id:"YouTube","onUpdate:modelValue":t[11]||(t[11]=s=>o.form.youtube=s),placeholder:"Youtube"},null,512),[[i,o.form.youtube]])])]),e("div",co,[y(d,{type:"button",class:"savebutton",onClick:t[12]||(t[12]=s=>o.ValidateEmail())},{default:w(()=>[g("Save")]),_:1})])])])])}var vo=c(M,[["render",uo],["__scopeId","data-v-4466ce1d"]]);export{vo as default};
