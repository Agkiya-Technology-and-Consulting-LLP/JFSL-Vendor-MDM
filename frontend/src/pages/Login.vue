<template>
  <section class="background-radial-gradient overflow-hidden">

    <div class="container px-4 py-5 px-md-5 text-center text-lg-start my-5">
      <div class="row gx-lg-5 align-items-center mb-5">
        <div class="col-lg-6 mb-5 mb-lg-0" style="z-index: 10">
          <h1 class="my-5 display-5 fw-bold ls-tight" style="color: hsl(218, 81%, 95%)">
            Welcome <br />
            <span style="color: hsl(218, 81%, 75%)">Reliance Supplier Portal</span>
          </h1>
        </div>

        <div class="col-lg-5 mb-5 mb-lg-0 position-relative">
          <div id="radius-shape-1" class="position-absolute rounded-circle shadow-5-strong"></div>
          <div id="radius-shape-2" class="position-absolute shadow-5-strong"></div>

          <div class="card bg-glass">

            <div class="card-body px-4 py-5 px-md-5" v-if="!show">
              <h1 style="color:blue ; text-align: center;">Welcome</h1>
              <p style="text-align: center; color: rgb(108, 108, 252);">Login with your Supplier ID</p>
              <form @submit.prevent="submit">
                <!-- Email input -->
                <div class="form-outline mb-4">
                  <input required type="text" name="email" id="form3Example1" class="form-control" v-model="email"
                    placeholder="Supplier ID" />
                </div>
                <div class="form-outline mb-4">
                  <input required type="password" name="password" id="form3Example3" v-model="password"
                    class="form-control" placeholder="Enter Password" />
                </div>
                <!-- Submit button -->
                <button class="btn btn-primary btn-block mb-4" v-on:click="submit()" :disabled="!email || !password">
                  Login
                </button>

                <!-- Register buttons -->
                <div class="text-center">
                  <p>Not registered with us? <a style="color:blue" v-on:click="show=!show">Sign up</a></p>
                  <!-- <p>Not registered with us?  <router-link to="/account/signup"> SignUp</router-link></p> -->

                </div>
                <!-- <div >THis is Sighup Form</div> -->
              </form>
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
                    <option value="m/s">m/s</option>
                    <option value="master">Master</option>
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

                <button class="btn btn-primary btn-block mb-4" v-on:click="signUp()">
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
  </section>
</template>

<script >
// import axios from "axios" 
import { session } from '../data/session'
import { createResource } from 'frappe-ui'
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
      last_name:''
    }
  },
  methods: {
    submit() {
      console.log("submit")
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
  }
}
</script>
<style scoped>
.background-radial-gradient {
  padding: 2rem 3rem;
  display: flex;
  justify-content: space-between;
  background: url(https://supplierfirst.ril.com/user/login_bg.e04cfc7678e7f23182a3.jpg) no-repeat top left;
  height: 100vh;
}

.bg-glass {
  background-color: hsla(0, 0%, 100%, 0.9) !important;
  backdrop-filter: saturate(200%) blur(25px);
}
</style>