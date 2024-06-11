<template>
  <section class="background-radial-gradient overflow-hidden">

    <div class="container px-4 py-5 px-md-5 text-center text-lg-start my-5">
      <div class="row gx-lg-5 align-items-center mb-5">
        <div class="col-lg-6 mb-5 mb-lg-0" style="z-index: 10">
          <div class="bg-image"><img src="../assets/Jio_Financial_Services_Logo.png" alt="Jio Image"></div>
          <h1 class="my-5 display-5 fw-bold ls-tight" style="color: hsl(218, 81%,50%)">
            Welcome to, JFSL Portal
            <!-- <span style="color: hsl(218, 81%, 60%)">JFSL Portal</span> -->
          </h1>
        </div>

        <div class="col-lg-5 mb-5 mb-lg-0 position-relative">
          <div id="radius-shape-1" class="position-absolute rounded-circle shadow-5-strong"></div>
          <div id="radius-shape-2" class="position-absolute shadow-5-strong"></div>

          <div class="card bg-glass">

            <!-- <div class="card-body px-4 py-5 px-md-5" v-if="!show">
              <h1 style="color:blue ; text-align: center;">Welcome</h1>
              <p style="text-align: center; color: rgb(108, 108, 252);">Login with your Supplier ID</p>
              <form @submit.prevent="submit">
                <div class="form-outline mb-4">
                  <input required type="text" name="email" id="form3Example1" class="form-control" v-model="email"
                    placeholder="Supplier ID" />
                </div>
                <div class="form-outline mb-4">
                  <input required type="password" name="password" id="form3Example3" v-model="password"
                    class="form-control" placeholder="Enter Password" />
                </div>
                <button class="btn btn-primary btn-block mb-4" v-on:click="submit()" :disabled="!email || !password">
                  Login
                </button>
                <div class="text-center">
                  <p>Not registered with us? <a style="color:blue" v-on:click="show=!show">Sign up</a></p>
                </div>
               
              </form>
             
            </div> -->
            
            <div class="card-body px-4 py-5 px-md-5" v-if="!show && !userExists">
              <h1 style="color:blue ; text-align: center;">Welcome</h1>
              <p style="text-align: center; color: rgb(108, 108, 252);">Login with your Supplier ID</p>
              <!-- <form > -->
                <div class="form-outline mb-4">
                      <input required type="text" name="email" id="form3Example1" class="form-control" v-model="email"
                        placeholder="Supplier ID" />
                    </div>

                <button class="btn btn-primary btn-block mb-4" v-on:click="checkUserExists()" :disabled="!email ">
                  Login
                </button>
                <!--<div class="text-center">
                  <p>Not registered with us? <a style="color:blue" v-on:click="show=!show">Sign up</a></p>
                </div>-->
              <!-- </form> -->
              </div>

              <div class="card-body px-4 py-5 px-md-5" v-if="userExists && !enter_otp">
              <h1 style="color:blue ; text-align: center;">Welcome</h1>
              <p style="text-align: center; color: rgb(108, 108, 252);">Select Agent and OTP delivery method.</p>
              <!-- <form > -->
                <div class="form-outline mb-4">
                <label>
                  <input required type="radio" name="email" class="" v-model="email_otp_send" value="otpSendtoEmail" />
                   &nbsp; Email: {{ email }}
                </label><br>
                <!--<label>
                  <input required type="radio" name="email" class="" v-model="email_otp_send" value="otpSendtoMobile" />
                  &nbsp; Mobile: {{ mobile_no  }}
                </label><br>
                <label>
                  <input required type="radio" name="email" class="" v-model="email_otp_send" value="otpSendtoBoth" />
                  &nbsp; Both: Email {{ eamil }} & Mobile {{ mobile_no }}
                </label><br>
                -->
              </div>
              <!-- <p>{{ otpmessage }}</p> -->
                <button class="btn btn-primary btn-block mb-4" v-on:click="send()" :disabled="!email_otp_send ">
                  Continue
                </button>
                <!-- <div class="text-center">
                  <p>Not registered with us? <a style="color:blue" v-on:click="()=>{show=!show; userExists=!userExists}">Sign up</a></p>
                </div> -->
              <!-- </form> -->
              </div>
              

              <div class="card-body px-4 py-5 px-md-5" v-if="enter_otp">
              <h1 style="color:blue ; text-align: center;">Welcome</h1>
                <div class="form-outline mb-4" v-if="enter_otp">
                  <input required type="text" name="emailotp" id="emailotp" class="form-control" v-model="emailotp"
                    placeholder="Enter otp" />
                </div>
                <button class="btn btn-primary btn-block mb-4" v-if="enter_otp" v-on:click="logintoportal()" >
                  Next
                </button>
                </div>


            <div class="card-body px-4 py-5 px-md-5" v-if="show && !varified">
              <h1 style="color:blue ; text-align: center;">Sign Up</h1>
              <p style="text-align: center; color: rgb(108, 108, 252);">Kindly enter your Email ID to proceed</p>
              <form>
                <!-- Email input -->
                <div class="form-outline mb-4" v-if="!options">
                  <input required type="text" name="email" id="form3Example2" class="form-control" v-model="email"
                    placeholder="Enter Your Email ID" />
                </div>

                <button class="btn btn-primary btn-block mb-4" v-on:click="sendOTP()" :disabled="!email" v-if="!options">
                  Next
                </button>
                <div>
                  <p v-if="otpsent" style="color:green;font-size: small;">Otp Set to your Email Id</p>
                </div>
                <div class="form-outline mb-4" v-if="options">
                  <input required type="text" name="emailotp" id="emailotp" class="form-control" v-model="emailotp"
                    placeholder="Enter otp" />
                </div>
                <button class="btn btn-primary btn-block mb-4" v-if="options" v-on:click="updated()">
                  Next
                </button>

                <!-- Register buttons -->
                <div class="text-center">
                  <p>Already registered with us? <a style="color:blue" v-on:click="show=!show">Sign In instead</a></p>
                  <!-- <p>Not registered with us?  <router-link to="/account/signup"> SignUp</router-link></p> -->

                </div>
              </form>

            </div>

            <div class="card-body px-4 py-5 px-md-5" v-if="varified">
              <h1 style="color:blue ; text-align: center;">Success</h1>
              <p style="text-align: center; color: rgb(108, 108, 252);">Your Email has been verified!<br>
                Kindly register here.</p>
              <form>
                <!-- Email input -->
                <div class="form-outline mb-4" >
                  <input required type="text" name="email" id="form3Example3" class="form-control" v-model="email"
                    readonly placeholder="Enter Your Email ID" style="background-color: #eeeeeeb2;" />
                </div>
                <div class="form-outline mb-4">
                  <select required name="title" id="form3Example4" class="form-control" v-model="title" placeholder="select title">
                    <option value="" selected>Select title</option>
                    <option value="m/s">Mr.</option>
                    <option value="master">Mister</option>
                    <option value="miss">Miss</option>
                  </select>
                </div>
                <div class="form-outline mb-4" >
                  <input required type="text" name="first_name" id="form3Example5" class="form-control"
                    v-model="first_name" placeholder="First Name" />
                </div>
                <div class="form-outline mb-4" >
                  <input required type="text" name="last_name" id="form3Example6" class="form-control" v-model="last_name"
                    placeholder="Last Name" />
                </div>
                <div class="form-outline mb-4" >
                  <input required type="text" name="mobile_no" id="form3Example6" class="form-control" v-model="mobile_no"
                    placeholder="Mobile Number" />
                </div>

                <button class="btn btn-primary btn-block mb-4" v-on:click="newUser()">
                  Register
                </button>

                <!-- Register buttons -->
                <div class="text-center">
                  <p>Already registered with us? <a style="color:blue" v-on:click="show=!show">Sign In instead</a></p>
                  <!-- <p>Not registered with us?  <router-link to="/account/signup"> SignUp</router-link></p> -->

                </div>
              </form>

            </div>
          </div>
        </div>
      </div>
    </div>
    <div>
    <!-- Tost Error Message -->
    <div class="toast align-items-center text-white bg-danger  border-0 show" role="alert" aria-live="assertive" aria-atomic="true" v-if="errormessage">
        <div class="d-flex">
            <div class="toast-body">
                User Not Exists.
            </div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" @click="hideErrorToast" aria-label="Close"></button>
        </div>
    </div>
    </div>
  </section>
</template>

<script >
// import axios from "axios" 
import { session } from '../data/session'
import { createResource ,toast} from 'frappe-ui'

export default {
  name: 'Login',
  data() {
    return {
      show: false,
      email: '',
      password: '',
      options: false,
      otpsent: false,
      varified: false,
      title:'',
      first_name:'',
      mobile_no:'',
      last_name:'',
      otp:'',
      userExists:false,
      email_otp_send:'',
      enter_otp:false,
      errormessage:false,
      otpmessage:''
    }
  },
  methods: {
    submit() {
      //console.log("submit")
      // let formData = new FormData(e.target);
      session.login.submit({
        // email: formData.get('email'),
        email: this.email,
        password: this.password,

        // password: formData.get('password'),
      });
    },
    async signUp() {
      // this.show = !this.show;
      try {
        const user = await createResource({
          url: 'frappe.core.doctype.user.user.sign_up',
          
          params: {
            email: this.email,
            full_name: this.first_name+' ' +this.last_name,
            mobile_no: this.mobile_no,
            first_name:this.first_name,
            last_name:this.last_name,
            redirect_to: '',
            // recievedOtp: ""
          },
          auto: true,
        });
        if (user.status === 200) {
          console.log('User signed up successfully');
          console.log(user.data);
        } else {
          console.error('Failed to sign up:', user.statusText);
        }
      } catch (error) {
        console.log(error);
      }
    },
    async sendOTP() {
      try {
        this.options = !this.options;

        const otp = await createResource({
          url: "jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.new",
          makeParams: () => ({
            doc: {
              email: this.email
            }
          }),
          auto: true,
          onSuccess: (data) => {
            this.otpsent = true
            this.recievedOtp = data.email_otp
            console.log(this.recievedOtp);
          },
          onError: (error) => {
            console.error("Error:", error);
          }
        });
      } catch (error) {
        console.error("Exception:", error);
      }
    },


    async sendOTPLogin() {
      try {
        this.options = !this.options;

        const otp = await createResource({
          url: "jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.request_verification_code",
          makeParams: () => ({
            
              email: this.email
            
          }),
          auto: true,
          onSuccess: (data) => {
            this.otpsent = true
            this.recievedOtp = data.email_otp
            console.log(this.recievedOtp);
          },
          onError: (error) => {
            console.error("Error:", error);
          }
        });
      } catch (error) {
        console.error("Exception:", error);
      }
    },

    async login() {
      try {
        this.options = !this.options;

        const otp = await createResource({
          url: "jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.verify_code_and_login",
          makeParams: () => ({
            
              email: this.email,
              verification_code:this.otp
            
          }),
          auto: true,
          onSuccess: (data) => {
            this.otpsent = true
            this.recievedOtp = data.email_otp
            console.log(data);
          },
          onError: (error) => {
            console.error("Error:", error);
          }
        });
      } catch (error) {
        console.error("Exception:", error);
      }
    },
    updated() {
    if (this.emailotp) {
      if (this.recievedOtp == this.emailotp) {
        this.otpsent = false
        this.varified = true
        console.log("Verified")
      } else {
        console.log("invalid ")
      }
    }
  },
  logintoportal(){
    if (this.emailotp) {
      if (this.recievedOtp == this.emailotp) {
        this.otpsent = false
        // this.varified = true
        this.loginwithoutpass()
        console.log("Verified")
      } else {
        console.log("invalid ")
      }
    }
  },
  newUser() {
      try {
        const user = createResource({
          url: "jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.new_user",
          makeParams: () => ({
            doc: {
              email: this.email,
              // :this.title,
              first_name: this.first_name,
              last_name: this.last_name,
              mobile_no: this.mobile_no,
              // redirect_to:''
            }
          }),
          auto: true,
          onSuccess: (data) => {
            console.log(data);
          },
          onError: (error) => {
            console.error("this is Error:", error);
          }
        })
      } catch (error) {
        console.log(error)
      }
    },

    loginwithoutpass(){
      const user = createResource({
          url: "jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.login",
          makeParams: () => ({
            doc: {
              email: this.email,
            }
          }),
          auto: true,
          onSuccess: (data) => {
            if (data) {
              let url = window.location.origin;
              const downloadUrl = url + "/frontend/?sid=" + data;
              let homeUrl = url + '/welcome';
              
              // Log the downloadUrl for debugging purposes
              console.log(downloadUrl);
              window.location.replace(url + '/frontend/welcome');
              // Replace the current URL with the download URL
              window.location.replace(downloadUrl);

              // If needed, replace the current URL with the home URL afterwards
              // You may want to set a delay or some condition here if both actions are required
              setTimeout(() => {
                window.location.replace(url + '/frontend/welcome');
              }, 1000); // Adjust the delay as needed
            }

              
          },
          onError: (error) => {
            console.error("this is Error:", error);
            toast({
              title: "Error",
              text: `User is not exists`,
              icon: "alert-circle",
              position: "bottom-center",
              iconClasses: "text-red-500",
            })
          }
        })
    },
    sendOTPforLogintoEmail() {
      const us = createResource({
        url: "jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.check",
        makeParams: () => ({
          doc: {
            email: this.email
          }
        }),
        auto: true,
        onSuccess: (data) => {
          console.log(data);
          this.enter_otp=true
          this.recievedOtp=data.email_otp
          this.otpmessage="OTP send to your mail"
        },
        onError: (error) => {
          console.error('Error:', error);
          // alert(`An error occurred: ${error.message}`);
          toast({
              title: "Error",
              text: `User is not exists`,
              icon: "alert-circle",
              position: "bottom-center",
              iconClasses: "text-red-500",
            })
        }
      });
    },
    checkUserExists(){
      const user_exists = createResource({
        url: "jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.checkUserExists",
        makeParams: () => ({
          doc: {
            email: this.email
          }
        }),
        auto: true,
        onSuccess: (data) => {
          if (data){
            console.log(data);
            this.userExists=true
            this.mobile_no=data.mobile_no
          }else{
            // alert("User Not Registered")
            
          }
          
        },
        onError: (error) => {
          console.error('Error:', error);
          // alert(`An error occurred: ${error.message}`);
          this.errormessage=true
          setTimeout(() => {
            this.errormessage=false
              }, 2000);
          toast({
              title: "Error",
              text: `User is not exists`,
              icon: "alert-circle",
              position: "bottom-center",
              iconClasses: "text-red-500",
            })
        }
      });
    },
    send(){
      console.log(this.email_otp_send)
      if(this.email_otp_send=="otpSendtoEmail"){
        this.enter_otp=true
        this.sendOTPforLogintoEmail()
      }
    }
  }
  // updated() {
  //   if (this.emailotp) {
  //     if (this.recievedOtp == this.emailotp) {
  //       this.otpsent = false
  //       this.varified = true
  //       console.log("Verified")
  //     } else {
  //       console.log("invalid ")
  //     }
  //   }
  // }
}
</script>
<style scoped>
.background-radial-gradient {
  /* padding: 2rem 3rem; */
  display: flex;
  justify-content: space-between;
  /* background: url("../assets/Jio_Financial_Services_Logo.png")no-repeat; */
  height: 100vh;
}

.bg-glass {
  background-color: hsla(0, 0%, 100%, 0.9) !important;
  backdrop-filter: saturate(200%) blur(25px);
}
.bg-image img{
  margin-left: 5rem;
  width: 50%;
  height: auto;
}

/* tost css */

.savebutton {
    background-color: #2e6bdc;
    color: white;
    font-size: 1.5rem;
    padding: 0px 20px 0px 20px;
    border-radius: 10px;
}

.toast {
    position: fixed;
    top: 5rem;
    right: 2rem;
    opacity: 0;
    transition: opacity 0.3s ease-in-out;
}

.toast.show {
    opacity: 1;
}
</style>