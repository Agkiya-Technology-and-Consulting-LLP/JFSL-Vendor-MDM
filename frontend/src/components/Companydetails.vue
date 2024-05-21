<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-12">

                <div class="bg-primary text-white p-1 rounded-top">
                    <h5>Select the Primary Company you are registering for</h5>
                </div>
                <div class="row mt-3">
                    <div class="col-md-3 mb-3">
                        <label for="company" class="form-label">Company</label>
                        <select class="form-control" id="company" v-model="form.company">
                            <option value="" disabled selected>Select Company</option>
                            <option value="Agkiya">Agkiya</option>
                            <option value="SMB">SMB</option>
                            <option value="Jio Finanace Limited">Jio Finanace Limited</option>
                            <option value="Jio Information Aggregator Services Ltd">Jio Information Aggregator Services Ltd</option>
                            <option value="JIO Insurance Broking Limited">JIO Insurance Broking Limited</option>
                            <option value="Jio Payment Solutions Limited">Jio Payment Solutions Limited</option>
                            <option value="JIO Payments Bank Limited">JIO Payments Bank Limited</option>
                            <option value="Petroleum Trust">Petroleum Trust</option>
                            <option value="JIO INFRASTRUCTURE MANAGEMENT SERVICE LIMITED">JIO INFRASTRUCTURE MANAGEMENT SERVICE LIMITED</option>
                            <option value="Reliance Services and Holding Limited">Reliance Services and Holding Limited</option>
                            <option value="Reliance Strategic Investments Limited">Reliance Strategic Investments Limited</option>

                        </select>
                    </div>
                    <div class="col-md-9 mb-3 mt-4">
                        <p>Select Comapny you are registering for</p>
                    </div>
                    
                    </div>

                    <div class="bg-primary text-white p-1 rounded-top">
                    <h5>Company Details</h5>
                </div>

                <div class="row mt-3">
                    

                    <div class="col-md-4 mb-3" :class="{ 'has-error': touched.company_name && !form.company_name }">
                        <label for="companyName" class="form-label">Company Name <span class="text-danger">*</span></label>
                        <input type="text" class="form-control" id="companyName" v-model="form.company_name"
                            placeholder="Company Name" @blur="touched.company_name = true">
                            <div v-if="touched.company_name && !form.company_name" class="text-danger">
                            Company Name is required.
                        </div>
                    </div>

                    <div class="col-md-4 mb-3">
                        <label for="companyType" class="form-label">Company Type<span class="text-danger">*</span></label>
                        <select name="" id="companyType" class="form-control" v-model="form.company_type">
                            <option value="M/S">M/S</option>
                        </select>
                    </div>

                    <div class="col-md-4 mb-3">
                        <label for="registrationNumber" class="form-label">Company Registration Number</label>
                        <input type="text" class="form-control" id="registrationNumber"
                            v-model="form.company_registration_number" placeholder="Company Number">
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col-md-3 mb-3">
                        <label for="Registration" class="form-label">Small Scale Industries Registration No.</label>
                        <input type="text" class="form-control" id="Registration"
                            v-model="form.small_scale_industries_registration_no"
                            placeholder="Small Scale Industries Registration No.">
                    </div>

                    <div class="col-md-3 mb-3">
                        <label for="Establishment" class="form-label">Date Of Establishment<span class="text-danger">*</span></label>
                        <input type="date" class="form-control" id="Establishment" placeholder="Date Of Establishment"
                            v-model="form.date_of_establishment">
                    </div>

                    <div class="col-md-3 mb-3">
                        <label for="about_company" class="form-label">About Company</label>
                        <textarea class="form-control" id="about_company" v-model="form.about_company" placeholder="About Company"></textarea>
                    </div>

                    <div class="col-md-3 mb-3">
                        <label for="D & B-N-D-I Number" class="form-label">D & B-N-D-I Number</label>
                        <input type="text" class="form-control" id="D & B-N-D-I Number" v-model="form.d_b_n_d_i_number"
                            placeholder="D & B-N-D-I Number">
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col-md-3 mb-3">
                        <label for="Logo" class="form-label">Logo</label>
                        <input type="file" class="form-control" id="Logo">
                    </div>

                    <div class="col-md-3 mb-3">
                        <label for="Company Turnover" class="form-label">Company Turnover</label>
                        <select name="" id="Company Turnover" class="form-control" v-model="form.company_turnover">
                            <option value=">250000000">>250000000</option>
                            <option value=">10000000">>10000000</option>
                            <option value=">50000000">>50000000</option>
                            <option value="<5000000"><5000000 </option>
                        </select>
                    </div>

                    <div class="col-md-3 mb-3">
                        <label for="Company Size" class="form-label">Company Size</label>
                        <select name="" id="Company Size" class="form-control"  v-model="form.company_size">
                            <option value="Large Scale">Large Scale</option>
                            <option value="Mid Scale">Mid Scale</option>
                            <option value="Small Scale">Small Scale</option>
                            <option value="Micro">Micro</option>
                        </select>
                    </div>

                    <div class="col-md-3 mb-3">
                        <label for="Small Scale" class="form-label">Natl. Small Scale Industries Rg No.</label>
                        <input type="text" class="form-control" id="Small Scale"
                            v-model="form.natl_small_scale_industries_registration_no"
                            placeholder="Small Scale registration no">
                    </div>
                </div>

                <div class="row mt-3">
                    <h6>Certification</h6>
                    <div class="col-md-3 mb-3">
                        <input type="checkbox" class="form-check-input mr-2" id="iso 9001" v-model="form.iso_9001_2000">
                        <label for="iso 9001" class="form-check-label"  >ISO 9001-2000</label>
                    </div>

                    <div class="col-md-3 mb-3">
                        <input type="checkbox" id="iso 4000" class="form-check-input mr-2" v-model="form.iso_4000">
                        <label for="iso 4000" class="form-check-label" >ISO 4000</label>
                    </div>

                    <div class="col-md-3 mb-3">
                        <input type="checkbox" id="HAS 18000" class="form-check-input mr-2" v-model="form.has_18000">
                        <label for="HAS 18000" class="form-check-label">HAS 18000</label>
                    </div>

                    <div class="col-md-3 mb-3">
                        <input type="checkbox" id="Any" class="form-check-input mr-2"
                            v-model="form.any_other_certification">
                        <label for="Any" class="form-check-label">Any other Certification</label>
                    </div>
                </div>

                <div class="bg-primary text-white p-1 rounded-top mt-2 d-flex justify-content-between">
                    <h5>PAN Details</h5>
                    <button @click="toggleCollapse1">
                        <i class="h-5 fa-solid fa-circle-chevron-down"></i>
                        <!-- <i :class="['h-5', 'fa-solid', 'fa-circle-chevron-down', { 'rotate-icon': isCollapsed1 }]"></i> -->
                    </button>
                </div>

                <div class="row mt-3" v-if="!isCollapsed1">
                    <div class="col-md-4 mb-3">
                        <label for="pan" class="form-label">Permanent account number <span class="text-danger">*</span></label>
                        <input type="text" class="form-control" id="pan" v-model="form.permanent_account_number"
                            placeholder="Enter PAN No">
                    </div>

                    <div class="col-md-4 mb-3">
                        <label for="Ownership" class="form-label">Ownership information</label>
                        <input type="text" class="form-control" id="Ownership" v-model="form.ownership_information"
                            placeholder="Ownership information">

                    </div>

                    <div class="col-md-4 mb-3">
                        <label for="Proprietor" class="form-label">Proprietor's Name<span class="text-danger">*</span></label>
                        <input type="text" class="form-control" id="Proprietor" v-model="form.proprietors_name"
                            placeholder="Proprietor's Name">
                    </div>
                </div>

                <div class="bg-primary text-white p-1 rounded-top mt-2 d-flex justify-content-between">
                    <h5>GST(Goods & Services )</h5>
                    <button @click="toggleCollapse2">
                        <i class="h-5 fa-solid fa-circle-chevron-down"></i>
                    </button>
                </div>

                <div class="row mt-3" v-if="!isCollapsed2">
                    <div class="col-md-6 mb-3">
                        <label for="GST" class="form-label">GST Registration  <span class="text-danger">*</span></label>
                        <input type="text" class="form-control" id="GST" v-model="form.gst_registration_number"
                            placeholder="Enter GST No">
                    </div>

                    <div class="col-md-6 mb-3">
                        <label for="valid" class="form-label">GST valid from <span class="text-danger">*</span></label>
                        <input type="date" class="form-control" id="valid" v-model="form.gst_valid_from">

                    </div>

                    <div class="col-md-6 mb-3">
                        <label for="GST Status" class="form-label">GST Status<span class="text-danger">*</span></label>
                        <!-- <input type="text" class="form-control" id="GST Status" v-model="form.gst_status"
                            placeholder="GST Status"> -->
                        <select name="gst_status" id="gst_status" class="form-control"  v-model="form.gst_status">
                            <option value="1. Normal Registered">1. Normal Registered</option>
                            <option value="2. Composition">2. Composition</option>
                            <option value="3. Casual">3. Casual</option>
                            <option value="5. Government/LocalAuthority">5. Government/LocalAuthority</option>
                            <option value="6. SEZ">6. SEZ</option>
                            <option value="7. EOU">7. EOU</option>
                            <option value="8. Unregistered">8. Unregistered</option>
                            <option value="9. overseas Vendor">9. overseas Vendor</option>
                            <option value="A. TAN Base GST">A. TAN Base GST</option>
                            <option value="B. Unknown">B. Unknown</option>
                            <option value="Z. One Time GST Registered">Z. One Time GST Registered</option>

                        </select>
                    </div>

                    <div class="col-md-6 mb-3">
                        <label for="GST Status " class="form-label">GST Status valid from<span class="text-danger">*</span></label>
                        <input type="date" class="form-control" id="GST Status " v-model="form.gst_status_valid_from">
                    </div>
                </div>

                <div class="bg-primary text-white p-1 rounded-top mt-2 d-flex justify-content-between">
                    <h5>CIN</h5>
                    <button @click="toggleCollapse3">
                        <i class="h-5 fa-solid fa-circle-chevron-down"></i>
                    </button>
                </div>

                <div class="row mt-3" v-if="!isCollapsed3">
                    <div class="col-md-6 mb-3">
                        <label for="CIN" class="form-label">CIN</label>
                        <input type="text" class="form-control" id="CIN" placeholder="Enter CIN No" v-model="form.cin">
                    </div>
                </div>

                <div class="bg-primary text-white p-1 rounded-top mt-2 d-flex justify-content-between">
                    <h5>Address & Residential Details</h5>
                    <button @click="toggleCollapse4">
                        <i class="h-5 fa-solid fa-circle-chevron-down"></i>
                    </button>
                </div>

                <div v-if="!isCollapsed4">
                    <h6 class="mt-3">Registered Address </h6>
                    <div class="row mt-3">
                        <div class="col-md-3 mb-3">
                            <label for="Name" class="form-label">Name</label>
                            <input type="text" class="form-control" id="Name" v-model="form.name_" placeholder="Name">
                        </div>
                        <div class="col-md-3 mb-3">
                            <label for="Address(Line 1)" class="form-label">Address(Line 1)</label>
                            <input type="text" class="form-control" id="Address(Line 1)" v-model="form.addressline_1"
                                placeholder="Address(Line 1)">
                        </div>
                        <div class="col-md-3 mb-3">
                            <label for="Address(Line 2)" class="form-label">Address(Line 2)</label>
                            <input type="text" class="form-control" id="Address(Line 2)" v-model="form.addressline_2"
                                placeholder="Address(Line 2)">
                        </div>
                        <div class="col-md-3 mb-3">
                            <label for="Address(Line 3)" class="form-label">Address(Line 3)</label>
                            <input type="text" class="form-control" id="Address(Line 3)" v-model="form.addressline_3"
                                placeholder="Address(Line 3)">
                        </div>

                    </div>

                    <div class="row mt-3">
                        <div class="col-md-3 mb-3">
                            <label for="Country" class="form-label">Country</label>
                            <input type="text" class="form-control" id="Country" v-model="form.country"
                                placeholder="Country">
                        </div>

                        <div class="col-md-3 mb-3">
                            <label for="City" class="form-label">City</label>
                            <input type="text" class="form-control" id="City" v-model="form.city" placeholder="City">
                        </div>

                        <div class="col-md-3 mb-3">
                            <label for="" class="form-label">Region</label>
                            <input type="text" class="form-control" id="Region" v-model="form.region"
                                placeholder="Region">
                        </div>

                        <div class="col-md-3 mb-3">
                            <label for="" class="form-label">Pincode</label>
                            <input type="text" class="form-control" id="Pincode" v-model="form.pincode"
                                placeholder="Pincode">
                        </div>
                    </div>

                    <h6 class="mt-3">Residential Details</h6>
                    <div class="row mt-3">
                        <div class="col-md-6 mb-3">
                            <label for="Residential Status" class="form-label">Residential Status</label>
                            <select name="Residential Status" id="Residential Status" class="form-control"
                                v-model="form.residential_status">
                                <option value="Resident of India">Resident of India</option>
                                <option value="Non-Resident of India">Non-Resident of India</option>
                                <option value="Foreign company having branch in india">Foreign company having branch in india</option>
                            </select>
                        </div>
                        <div class="col-md-6 mb-3">
                            <label for="TIN" class="form-label">Tax Identification No. (TIN)</label>
                            <input type="text" class="form-control" id="TIN" v-model="form.tax_identification_no_tin"
                                placeholder="TIN No">
                        </div>
                    </div>

                    <div class="row mt-3">
                        <div class="col-md-4 mb-3">
                            <label for="Permanent Account No." class="form-label">Permanent Account No.</label>
                            <input type="text" class="form-control" id="Permanent Account No."
                                v-model="form.permanent_account_no" placeholder="Permanent Account No.">
                        </div>

                        <div class="col-md-4 mb-3">
                            <label for="Tax Category" class="form-label">Tax Category</label>
                            <!-- <input type="text" class="form-control" id="Tax Category" placeholder="Tax Category"
                                v-model="form.tax_category"> -->

                            <select name="tax_category" id="tax_category" class="form-control"
                                v-model="form.tax_category">
                                <option value="Registered Composition">Registered Composition</option>
                                <option value="Reverse Charge Out-State">Reverse Charge Out-State</option>
                                <option value="Reverse Charge In-State">Reverse Charge In-State</option>
                                <option value="Out-State">Out-State</option>
                                <option value="In-State">In-State</option>
                            </select>
                        </div>

                        <div class="col-md-4 mb-3">
                            <label for="Tax Withholding Category" class="form-label">Tax Withholding Category</label>
                            <input type="text" class="form-control" id="Tax Withholding Category"
                                v-model="form.tax_withholding_category" placeholder="Tax Withholding Category">
                        </div>
                    </div>
                </div>



                <div class="bg-primary text-white p-1 rounded-top mt-2 d-flex justify-content-between">
                    <h5>Sales Tax, ESI, PF, MSMED And WCT Details</h5>
                    <button @click="toggleCollapse">
                        <i :class="['h-5', 'fa-solid', 'fa-circle-chevron-down', { rotate: isCollapsed }]"></i>
                    </button>
                </div>
                <div v-if="!isCollapsed">
                    <h6 class="mt-3">Sales Tax</h6>
                    <div class="row mt-3">
                        <div class="col-md-6 mb-3">
                            <label for="Supplier under VAT" class="form-label">Type of Supplier under
                                VAT</label>
                            <select name="Supplier under VAT" id="Supplier under VAT" class="form-control"
                                v-model="form.type_of_supplier_under_vat">
                                <option value="Registered Dealer">Registered Dealer</option>
                                <option value="Unregistered Dealer">Unregistered Dealer</option>
                                <option value="Incentive Unit">Incentive Unit</option>
                                <option value="Notified Oil Company">Notified Oil Company</option>
                                <option value="SEZ unit">SEZ unit</option>
                                <option value="EQU">EQU</option>
                                <option value="Vendor under threshold unit">Vendor under threshold unit</option>
                                <option value="Foreign vendor">Foreign vendor</option>
                            </select>
                        </div>
                        <div class="col-md-6 mb-3">
                            <label for="CST Number" class="form-label">CST Number</label>
                            <input type="text" class="form-control" id="CST Number" v-model="form.cst_number"
                                placeholder="CST Number">
                        </div>
                    </div>



                    <div class="row mt-3">
                        <div class="col-md-4 mb-3">
                            <label for="LST Number" class="form-label">LST Number</label>
                            <input type="text" class="form-control" id="LST Number" v-model="form.lst_number"
                                placeholder="LST Number">
                        </div>

                        <div class="col-md-4 mb-3">
                            <label for="Date for CST" class="form-label">Registration Date for CST</label>
                            <input type="date" class="form-control" id="Date for CST"
                                v-model="form.resistration_date_cst" placeholder="Date for CST">
                        </div>

                        <div class="col-md-4 mb-3">
                            <label for="Date for LST" class="form-label">Registration Date for LST</label>
                            <input type="date" class="form-control" id="Date for LST"
                                v-model="form.registration_date_lst" placeholder="Date for LST">
                        </div>
                    </div>

                    <h6 class="mt-3">ESI (Employee State Insurance)</h6>
                    <div class="row mt-3">
                        <div class="col-md-6 mb-3">
                            <label for="ESI Number" class="form-label">ESI Number</label>
                            <input type="text" class="form-control" id="ESI Number" v-model="form.esi_number"
                                placeholder="ESI Number">
                        </div>
                    </div>

                    <h6 class="mt-3">PF (Provident Fund)</h6>
                    <div class="row mt-3">
                        <div class="col-md-6 mb-3">
                            <label for="EPF Number" class="form-label">EPF Number</label>
                            <input type="text" class="form-control" id="EPF Number" v-model="form.epf_number"
                                placeholder="EPF Number">
                        </div>
                    </div>

                    <h6 class="mt-3">MSMED</h6>
                    <div class="row mt-3">
                        <div class="col-md-4 mb-3">
                            <label for="Enterprise type" class="form-label">Select your Enterprise type</label>
                            <select name="Enterprise type" id="Enterprise type"
                                v-model="form.select_your_enterprise_type" class="form-control">
                                <option value="Micro Enterprise">Micro Enterprise</option>
                                <option value="Small Enterprise">Small Enterprise</option>
                                <option value="Medium Enterprise">Medium Enterprise</option>
                            </select>
                        </div>

                        <div class="col-md-4 mb-3">
                            <label for="Certificate Number" class="form-label">MSME Certificate Number</label>
                            <input type="text" class="form-control" id="Certificate Number"
                                v-model="form.msme_certificate_number" placeholder="Certificate Number">
                        </div>

                        <div class="col-md-4 mb-3">
                            <label for="Udyam" class="form-label">Udyam Registration Number </label>
                            <input type="text" class="form-control" id="Udyam" placeholder="Udyam"
                                v-model="form.udyam_registration_number">
                        </div>
                    </div>

                    <h6 class="mt-3">WCT</h6>
                    <div class="row mt-3">
                        <div class="col-md-4 mb-3">
                            <label for="Enterprise type" class="form-label">WCT</label>
                            <input type="text" class="form-control" id="WCT" v-model="form.wct" placeholder="WCT">
                        </div>
                    </div>
                </div>




            </div>
            <div class="d-flex justify-content-end mt-4 mb-3">
                <Button type="button" class="savebutton" @click="ValidateEmail()">Save</Button>
            </div>
        </div>
    </div>


    <!-- Tost Message -->
    <div
      class="toast align-items-center text-white bg-success  border-0"
      role="alert"
      aria-live="assertive"
      aria-atomic="true"
      :class="{ 'show': showToast }"
    >
      <div class="d-flex">
        <div class="toast-body">
          Details Saved Sucessfully.
        </div>
        <button
          type="button"
          class="btn-close btn-close-white me-2 m-auto"
          @click="hideToast"
          aria-label="Close"
        ></button>
      </div>
    </div>
</template>

<!-- <script>
export default {
};
</script> -->
<script>
import { ref, defineComponent, onMounted,watch, reactive,computed } from "vue";
import { sessionUser } from "../data/session";
import { createResource } from 'frappe-ui';
const showToast = ref(false);



export default defineComponent({
    name: 'ContactDetails',
    setup() {

        const isCollapsed = ref(true);
        const toggleCollapse = () => {
            isCollapsed.value = !isCollapsed.value;
        };
        const isCollapsed1 = ref(true);
        const toggleCollapse1 = () => {
            isCollapsed1.value = !isCollapsed1.value;
        };
        const isCollapsed2 = ref(true);
        const toggleCollapse2 = () => {
            isCollapsed2.value = !isCollapsed2.value;
        };
        const isCollapsed3 = ref(true);
        const toggleCollapse3 = () => {
            isCollapsed3.value = !isCollapsed3.value;
        };
        const isCollapsed4 = ref(true);
        const toggleCollapse4 = () => {
            isCollapsed4.value = !isCollapsed4.value;
        };


        const form = reactive({
            company: '',
            company_name: '',
            company_type: '',
            company_registration_number: '',
            small_scale_industries_registration_no: '',
            date_of_establishment: '',
            docname: '',
            about_company: '',
            d_b_n_d_i_number: '',
            company_turnover: '',
            company_size: '',
            natl_small_scale_industries_registration_no: '',
            iso_9001_2000: 0,
            iso_4000: 0,
            has_18000: 0,
            any_other_certification: 0,
            permanent_account_number: '',
            ownership_information: '',
            proprietors_name: '',
            gst_registration_number: '',
            gst_valid_from: '',
            gst_status: '',
            gst_status_valid_from: '',
            cin: '',
            name_: '',
            addressline_1: '',
            addressline_2: '',
            addressline_3: '',
            country: '',
            city: '',
            region: '',
            pincode: '',
            residential_status: '',
            tax_identification_no_tin: '',
            permanent_account_no: '',
            tax_category: '',
            tax_withholding_category: '',
            type_of_supplier_under_vat: '',
            cst_number: '',
            lst_number: '',
            resistration_date_cst: '',
            registration_date_lst: '',
            esi_number: '',
            epf_number: '',
            select_your_enterprise_type: '',
            msme_certificate_number: '',
            udyam_registration_number: '',
            wct: '',
            pan:''

        });
        const touched = reactive({
            company_name: false,
        });
        const isValid = computed(() => {
            return  form.company_name;
        });

        const loginUser = sessionUser();

        onMounted(() => {
            const supplier = createResource({
                url: "jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.get_supplier_detail",
                makeParams: () => ({
                    doc: {
                        email: loginUser
                    }
                }),
                auto: true,
                onSuccess: (data) => {
                    console.log(data);
                    form.company = data.company;
                    form.company_name = data.company_name;
                    form.company_type = data.company_type;
                    form.company_registration_number = data.company_registration_number;
                    form.small_scale_industries_registration_no = data.small_scale_industries_registration_no;
                    form.date_of_establishment = data.date_of_establishment;
                    form.about_company = data.about_company;
                    form.d_b_n_d_i_number = data.d_b_n_d_i_number;
                    form.company_turnover = data.company_turnover;
                    form.company_size = data.company_size;
                    form.natl_small_scale_industries_registration_no = data.natl_small_scale_industries_registration_no;
                    if(data.iso_9001_2000){
                        form.iso_9001_2000 = true
                    }
                    if(data.iso_4000){
                        form.iso_4000 = true
                    }
                    if(data.has_18000){
                        form.has_18000 = true
                    }
                    if(data.any_other_certification){
                        form.any_other_certification = true
                    }
                    
                    form.permanent_account_number = data.permanent_account_number
                    form.ownership_information = data.ownership_information
                    form.proprietors_name = data.proprietors_name
                    form.gst_registration_number = data.gst_registration_number
                    form.gst_valid_from = data.gst_valid_from
                    form.gst_status = data.gst_status
                    form.gst_status_valid_from = data.gst_status_valid_from
                    form.cin = data.cin
                    form.name_ = data.name_
                    form.addressline_1 = data.addressline_1
                    form.addressline_2 = data.addressline_2
                    form.addressline_3 = data.addressline_3
                    form.country = data.country
                    form.city = data.city
                    form.region = data.region
                    form.pincode = data.pincode
                    form.residential_status = data.residential_status
                    form.tax_identification_no_tin = data.tax_identification_no_tin
                    form.permanent_account_no = data.permanent_account_no
                    form.pan = data.permanent_account_no
                    form.tax_category = data.tax_category
                    form.tax_withholding_category = data.tax_withholding_category
                    form.type_of_supplier_under_vat = data.type_of_supplier_under_vat
                    form.cst_number = data.cst_number
                    form.lst_number = data.lst_number
                    form.resistration_date_cst = data.resistration_date_cst
                    form.registration_date_lst = data.registration_date_lst
                    form.esi_number = data.esi_number
                    form.epf_number = data.epf_number
                    form.select_your_enterprise_type = data.select_your_enterprise_type
                    form.msme_certificate_number = data.msme_certificate_number
                    form.udyam_registration_number = data.udyam_registration_number
                    form.wct = data.wct
                    form.docname = data.name
                },
                onError: (error) => {
                    console.error('Error:', error);
                }
            });
        });
        const showToastMessage = () => {
            showToast.value = true;
            console.log("Details saved successfully");
            setTimeout(() => {
                showToast.value = false;
            }, 1000);
        };

        const hideToast = () => {
            showToast.value = false;
        };
        const ValidateEmail = () => {
            console.log('values are here', form);
            const supplier = createResource({
                url: "jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.save_supplier_detail",
                makeParams: () => ({
                    doc: {
                        company: form.company,
                        company_name: form.company_name,
                        company_type: form.company_type,
                        company_registration_number: form.company_registration_number,
                        small_scale_industries_registration_no: form.small_scale_industries_registration_no,
                        docname: form.docname,
                        date_of_establishment: form.date_of_establishment,
                        about_company: form.about_company,
                        d_b_n_d_i_number: form.d_b_n_d_i_number,
                        company_turnover: form.company_turnover,
                        company_size: form.company_size,
                        natl_small_scale_industries_registration_no: form.natl_small_scale_industries_registration_no,
                        iso_9001_2000: form.iso_9001_2000,
                        iso_4000: form.iso_4000,
                        has_18000: form.has_18000,
                        any_other_certification: form.any_other_certification,
                        permanent_account_number: form.permanent_account_number,
                        ownership_information: form.ownership_information,
                        proprietors_name: form.proprietors_name,
                        gst_registration_number: form.gst_registration_number,
                        gst_valid_from: form.gst_valid_from,
                        gst_status: form.gst_status,
                        gst_status_valid_from: form.gst_status_valid_from,
                        cin: form.cin,
                        name_: form.name_,
                        addressline_1: form.addressline_1,
                        addressline_2: form.addressline_2,
                        addressline_3: form.addressline_3,
                        country: form.country,
                        city: form.city,
                        region: form.region,
                        pincode: form.pincode,
                        residential_status: form.residential_status,
                        tax_identification_no_tin: form.tax_identification_no_tin,
                        permanent_account_no: form.permanent_account_no,
                        tax_category: form.tax_category,
                        tax_withholding_category: form.tax_withholding_category,
                        type_of_supplier_under_vat: form.type_of_supplier_under_vat,
                        cst_number: form.cst_number,
                        lst_number: form.lst_number,
                        resistration_date_cst: form.resistration_date_cst,
                        registration_date_lst: form.registration_date_lst,
                        esi_number: form.esi_number,
                        epf_number: form.epf_number,
                        select_your_enterprise_type: form.select_your_enterprise_type,
                        msme_certificate_number: form.msme_certificate_number,
                        udyam_registration_number: form.udyam_registration_number,
                        wct: form.wct
                    }
                }),
                auto: true,
                onSuccess: (data) => {
                    console.log(data)
                    showToastMessage()
                },
                onError: (error) => {
                    console.error('Error:', error);
                    alert(`An error occurred: ${error.message}`);
                }
            });

        };
        // watch(()=>form.permanent_account_number,
        // (value)=>{
        //     if (value){

        //     }
        // }
    // )
    watch( ()=>form.permanent_account_number,
            (newValue,oldValue)=>{
                if(oldValue && newValue!=oldValue){
                    try {
                    const response =  createResource({
                        url: 'jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.get_pan_details',
                        makeParams:()=>({
                            data: {
                            pan: newValue
                        },
                        }),
                        auto: true,
                        onSuccess :(data)=>{
                            console.log(data    )
                            form.proprietors_name = data.result.name;
                        },onError :(error)=>{
                            console.log(error)
                        }
                    });
                    } catch (error) {
                        console.error('Error fetching bank details:', error);
                    }

                    const typeMap = {
                        'P': 'Individual',
                        'C': 'Company',
                        'H': 'Hindu Undivided Family',
                        'A': 'Association of Persons',
                        'B': 'Body of Individuals',
                        'G': 'Government Agency',
                        'J': 'Artificial Juridical Person',
                        'L': 'Local Authority',
                        'F': 'Firm/Partnership',
                        'T': 'Trust'
                    };
                    const fourthChar = newValue.charAt(3).toUpperCase();
                    const panType = typeMap[fourthChar];
                    console.log(panType)
                    form.ownership_information = panType
                }
        })
watch(()=>form.company_turnover,
    (value)=>{
        console.log(value)
        if(value == ">250000000"){
            form.company_size ="Large Scale"
        }else if(value == ">10000000"){
            form.company_size ="Mid Scale"
        }else if(value == ">50000000"){
            form.company_size ="Small Scale"
        }else{
            form.company_size ="Micro"
        }
     })
        return {
            form,
            ValidateEmail,
            isCollapsed,
            toggleCollapse,
            isCollapsed1,
            toggleCollapse1,
            isCollapsed2,
            toggleCollapse2,
            isCollapsed3,
            toggleCollapse3,
            isCollapsed4,
            toggleCollapse4,
            touched,
            isValid,
            hideToast,
            showToastMessage,
            showToast
        };
    }
});
</script>

<style scoped>
.container {
    height: 80vh;
}

.bg-primary {
    background-color: #2e6bdc !important;
    height: 2rem;
}

.rounded-top {
    border-radius: 10px 10px 0px 0px;
}

.savebutton {
    background-color: #2e6bdc;
    color: white;
    font-size: 1.5rem;
    padding: 1rem;
}

label {
    font-weight: 600;
}

h6 {
    color: #2e6bdc;
    font-weight: bolder;
}
.rotate-icon {
  transform: rotate(180deg);
  transition: transform 0.3s ease;
}
.text-danger {
    color: red;
}

.has-error input,
.has-error select {
    border-color: red;
}

/* .has-error label {
    color: red;
} */
:disabled{
    background-color: grey;
    cursor:not-allowed;
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
