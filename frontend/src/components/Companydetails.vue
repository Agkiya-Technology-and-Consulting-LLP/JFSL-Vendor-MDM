<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-12">

                <!-- <div class="bg-primary text-white p-1 rounded-top">
                <h5>Select the Primary Company you are registering for</h5>
            </div>
            <div class="row mt-3">
              
                <div class="col-md-3 mb-3">
                    <label for="company" class="form-label">Company</label>
                    <select class="form-control" id="company" v-model="form.company">
                        <option v-for="category in form.companylist" :key="category.name" :value="category.name">
                            {{ category.name }}
                        </option>
                    </select>
                </div>
                <div class="col-md-9 mb-3 mt-4">
                    <p>Select Comapny you are registering for</p>
                </div>

            </div> -->

                <div class="bg-primary text-white p-1 rounded-top">
                    <h5>Company Details</h5>
                </div>

                <div class="row mt-3">

                    <div class="col-md-3 mb-3" :class="{ 'has-error': touched.company_name && !form.company_name }">
                        <label for="companyName" class="form-label">Company Name <span
                                class="text-danger">*</span></label>
                        <input type="text" class="form-control" id="companyName" v-model="form.company_name"
                            placeholder="Company Name" @blur="touched.company_name = true" :disabled="isReadonly">
                        <div v-if="touched.company_name && !form.company_name" class="text-danger">
                            Company Name is required.
                        </div>
                    </div>

                    <!-- <div class="col-md-4 mb-3">
                    <label for="companyType" class="form-label">Company Type<span class="text-danger">*</span></label>
                    <select name="" id="companyType" class="form-control" v-model="form.company_type">
                        <option value="M/S">M/S</option>
                    </select>
                </div> -->

                    <div class="col-md-3 mb-3">
                        <label for="registrationNumber" class="form-label">Company Registration Number</label>
                        <input type="text" class="form-control" id="registrationNumber"
                            v-model="form.company_registration_number" placeholder="Company Number" :disabled="isReadonly">
                    </div>



                    <div class="col-md-3 mb-3">
                        <label for="Registration" class="form-label">Small Scale Industries Registration No.</label>
                        <input type="text" class="form-control" id="Registration"
                            v-model="form.small_scale_industries_registration_no"
                            placeholder="Small Scale Industries Registration No." :disabled="isReadonly">
                    </div>

                    <div class="col-md-3 mb-3">
                        <label for="Establishment" class="form-label">Date Of Establishment</label>
                        <input type="date" class="form-control" id="Establishment" placeholder="Date Of Establishment"
                            v-model="form.date_of_establishment" :disabled="isReadonly">
                    </div>
                </div>
                <!-- <div class="col-md-3 mb-3">
                    <label for="Establishment" class="form-label">Date Of Establishment<span class="text-danger">*</span></label>
                    <input type="date" class="form-control" id="Establishment" placeholder="Date Of Establishment" v-model="form.date_of_establishment">
                </div> -->
                <div class="row mt-3">

                    <!-- <div class="col-md-3 mb-3">
                    <label for="nature_of_business" class="form-label">Nature Of Business</label>
                    <select name="" id="nature_of_business" class="form-control" v-model="form.nature_of_business" >
                        <option value="Professional Services">Professional Services</option>
                        <option value="Man Power">Man Power</option>
                        <option value="Goods & Materials">Goods & Materials</option>
                        <option value="IT">IT</option>
                        <option value="Consultancy">Consultancy</option>
                    </select>
                </div> -->

                </div>

                <div class="row mt-3">
                    <!-- <div class="col-md-3 mb-3">
                    <label for="D & B-N-D-I Number" class="form-label">D & B-N-D-I Number</label>
                    <input type="text" class="form-control" id="D & B-N-D-I Number" v-model="form.d_b_n_d_i_number" placeholder="D & B-N-D-I Number">
                </div> -->

                    <!-- <a href={{ form.logourl }}> See Attachment</a> -->
                    <div class="col-md-3 mb-3">
                        <label for="Company Turnover" class="form-label">Company Turnover</label>
                        <select name="" id="Company Turnover" class="form-control" v-model="form.company_turnover" :disabled="isReadonly">
                            <option value=">250000000">> 250000000</option>
                            <option value=">100000000">> 100000000</option>
                            <option value=">50000000">> 50000000</option>
                            <option value="<50000000">
                                < 50000000 </option>
                            <!-- <option value="<2000000">
                                < 2000000 </option> -->
                        </select>
                    </div>
                    <div class="col-md-3 mb-3">
                        <label for="Company Size" class="form-label">Company Size</label>
                        <select name="" id="Company Size" class="form-control" v-model="form.company_size" disabled :disabled="isReadonly">
                            <option value="Large Scale">Large Scale</option>
                            <option value="Mid Scale">Mid Scale</option>
                            <option value="Small Scale">Small Scale</option>
                            <option value="Micro">Micro</option>
                        </select>
                    </div>

                    <!-- <div class="col-md-3 mb-3">
                    <label for="Small Scale" class="form-label">Natl. Small Scale Industries Rg No.</label>
                    <input type="text" class="form-control" id="Small Scale" v-model="form.natl_small_scale_industries_registration_no" placeholder="Small Scale registration no">
                </div> -->
                </div>
                <!-- <div class="row mt-3">
                <div class="col-md-3 mb-3">
                    <label for="Logo" class="form-label">Logo</label>
                    <input type="file" class="form-control" id="Logo" @change="handleFileChange" >
                </div>
            </div> -->
                <div class="row mt-3">
                    <h6>Certification</h6>
                    <div class="col-md-3 mb-3">
                        <input type="checkbox" class="form-check-input mr-2" id="iso 9001" v-model="form.iso_9001_2000" :disabled="isReadonly">
                        <label for="iso 9001" class="form-check-label">ISO 9001-2000</label>
                    </div>

                    <div class="col-md-3 mb-3">
                        <input type="checkbox" id="iso 4000" class="form-check-input mr-2" v-model="form.iso_4000" :disabled="isReadonly">
                        <label for="iso 4000" class="form-check-label">ISO 4000</label>
                    </div>

                    <div class="col-md-3 mb-3">
                        <input type="checkbox" id="HAS 18000" class="form-check-input mr-2" v-model="form.has_18000" :disabled="isReadonly">
                        <label for="HAS 18000" class="form-check-label">HAS 18000</label>
                    </div>

                    <div class="col-md-3 mb-3">
                        <input type="checkbox" id="Any" class="form-check-input mr-2"
                            v-model="form.any_other_certification" :disabled="isReadonly">
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
                    <!-- <div class="col-md-4 mb-3">
                    <label for="pan" class="form-label">Permanent account number <span class="text-danger">*</span></label>
                    <input type="text" class="form-control" id="pan" v-model="form.permanent_account_number" placeholder="Enter PAN No">
                </div> -->

                    <div class="col-md-4 mb-3"
                        :class="{ 'has-error': touched.permanent_account_number && !form.permanent_account_number }">
                        <label for="pan" class="form-label">Permanent account number <span
                                class="text-danger">*</span></label>
                        <input type="text" class="form-control" id="pan" v-model="form.permanent_account_number"
                            placeholder="Enter PAN No" @blur="touched.permanent_account_number = true" :disabled="isReadonly">
                        <div v-if="touched.permanent_account_number && !form.permanent_account_number"
                            class="text-danger">
                            PAN is required.
                        </div>
                        <div v-if="form.error_message && form.permanent_account_number" class="text-danger">
                            {{ form.error_message }}.
                        </div>
                    </div>

                    <div class="col-md-4 mb-3">
                        <label for="Ownership" class="form-label">Ownership information</label>
                        <input type="text" class="form-control" id="Ownership" v-model="form.ownership_information"
                            placeholder="Ownership information" disabled>

                    </div>

                    <div class="col-md-4 mb-3">
                        <label for="Proprietor" class="form-label">Proprietor's Name</label>
                        <input type="text" class="form-control" id="Proprietor" v-model="form.proprietors_name" disabled
                            placeholder="Proprietor's Name">
                    </div>

                    <div class="col-md-4 mb-3">
                        <label for="is_aadhar_pan_linked" class="form-label">Is Aadhar PAN Linked <span
                                class="text-danger"></span></label>
                        <select name="" id="is_aadhar_pan_linked" class="form-control"
                            v-model="form.is_aadhar_pan_linked" disabled>
                            <option value="Yes">YES</option>
                            <option value="No">NO</option>
                        </select>
                    </div>

                </div>

                <div class="bg-primary text-white p-1 rounded-top mt-2 d-flex justify-content-between">
                    <h5>GST(Goods & Services )</h5>
                    <button @click="toggleCollapse2">
                        <i class="h-5 fa-solid fa-circle-chevron-down"></i>
                    </button>
                </div>
               
                <div class="row mt-3" v-if="!isCollapsed2">
                    <div class="col-md-3 mb-3">
                        <input type="checkbox" id="applicable_gst" class="form-check-input mr-2" v-model="form.applicable_gst" :disabled="isReadonly">
                        <label for="applicable_gst" class="form-check-label">Gst Applicable</label>
                    </div>
                    <div class="row mt-3" v-if="form.applicable_gst">
                        
                   
                    <!-- <div class="col-md-6 mb-3">
                    <label for="GST" class="form-label">GST Registration <span class="text-danger">*</span></label>
                    <input type="text" class="form-control" id="GST" v-model="form.gst_registration_number" placeholder="Enter GST No">
                </div> -->
                    <div class="col-md-6 mb-3">
                        <label for="GST" class="form-label">GST Registration <span
                            class="text-danger">*</span> </label>
                        <input type="text" class="form-control" id="GST" v-model="form.gst_registration_number"
                            placeholder="Enter GST No" @blur="touched.gst_registration_number = true" :disabled="isReadonly">
                        <div v-if="touched.gst_registration_number && !form.gst_registration_number"
                            class="text-danger">
                            GST Number is required.
                        </div>
                        <div v-if="form.gst_error" class="text-danger">
                            {{ form.gst_error }}
                        </div>
                    </div>

                    <div class="col-md-6 mb-3">
                        <label for="valid" class="form-label">GST valid from </label>
                        <input type="date" class="form-control" id="valid" v-model="form.gst_valid_from" disabled>

                    </div>

                    <!-- <div class="col-md-6 mb-3">
                    <label for="GST Status" class="form-label">GST Status<span class="text-danger">*</span></label>
                    <select name="gst_status" id="gst_status" class="form-control" v-model="form.gst_status" >
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
                </div> -->
                    <div class="col-md-6 mb-3" :class="{ 'has-error': touched.gst_status && !form.gst_status }">
                        <label for="GST Status" class="form-label">GST Status</label>
                        <select name="gst_status" id="gst_status" class="form-control" v-model="form.gst_status"
                            disabled @blur="touched.gst_status = true" :disabled="isReadonly">
                            <option value="Registered Regular">1. Registered Regular</option>
                            <option value="Registered Composition">2. Registered Composition</option>
                            <option value="Unregistered">3. Unregistered</option>
                            <option value="Overseas">5. Overseas</option>
                            <option value="SEZ">6. SEZ</option>
                            <option value="Deemed Export">7. Deemed Export</option>
                            <option value="UIN Holders">8. UIN Holders</option>
                            <option value="Tax Deductor">9. Tax Deductor</option>
                            <option value="Tax Collector">A. Tax Collector</option>
                            <!-- <option value="B. Unknown">B. Unknown</option>
                            <option value="Z. One Time GST Registered">Z. One Time GST Registered</option> -->
                        </select>
                        <div v-if="touched.gst_status && !form.gst_status" class="text-danger">
                            Enter gst status
                        </div>
                    </div>
                    <div class="col-md-6 mb-3">
                        <label for="GST Status Active" class="form-label">GST Status Active</label>
                        <select name="gst_status_active" id="gst_status_active" class="form-control"
                            v-model="form.gst_status_active" disabled>
                            <option value="Yes">Yes</option>
                            <option value="No">No</option>
                        </select>
                        <div v-if="touched.gst_status && !form.gst_status" class="text-danger">
                            Enter gst status
                        </div>
                    </div>

                    
                    <!-- <div class="col-md-6 mb-3">
                    <label for="GST Status " class="form-label">GST Status valid from<span class="text-danger">*</span></label>
                    <input type="date" class="form-control" id="GST Status " v-model="form.gst_status_active">
                </div> -->
                    <div class="col-md-6 mb-3">
                        <label for="legal_name_of_the_business" class="form-label">Legal Name of the Business </label>
                        <input type="text" class="form-control" id="legal_name_of_the_business"
                            v-model="form.legal_name_of_the_business" disabled>

                    </div>
                    <div class="col-md-6 mb-3">
                        <label for="constitution_of_business" class="form-label">Constitution of Business </label>
                        <input type="text" class="form-control" id="constitution_of_business"
                            v-model="form.constitution_of_business" disabled>

                    </div>
                    <div class="col-md-12 mb-3">
                        <label for="address_information_for_principal_place_of_business" class="form-label">Address
                            information for principal place of business </label>
                        <textarea class="form-control" id="address_information_for_principal_place_of_business"
                            v-model="form.address_information_for_principal_place_of_business" disabled></textarea>
                    </div>
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
                        <input type="text" class="form-control" id="CIN" placeholder="Enter CIN No" v-model="form.cin" :disabled="isReadonly">
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
                        <!-- <div class="col-md-3 mb-3">
                        <label for="Name" class="form-label">Name</label>
                        <input type="text" class="form-control" id="Name" v-model="form.name_" placeholder="Name">
                    </div> -->

                        <div class="col-md-3 mb-3" :class="{ 'has-error': touched.name_ && !form.name_ }">
                            <label for="Name" class="form-label">Name <span class="text-danger">*</span></label>
                            <input type="text" class="form-control" id="Name" v-model="form.name_" placeholder="Name"
                                @blur="touched.name_ = true" :disabled="isReadonly">
                            <div v-if="touched.name_ && !form.name_" class="text-danger">
                                Name is required.
                            </div>
                        </div>


                        <!-- <div class="col-md-3 mb-3">
                        <label for="Address(Line 1)" class="form-label">Address(Line 1)</label>
                        <input type="text" class="form-control" id="Address(Line 1)" v-model="form.addressline_1" placeholder="Address(Line 1)">
                    </div> -->

                        <div class="col-md-3 mb-3"
                            :class="{ 'has-error': touched.addressline_1 && !form.addressline_1 }">
                            <label for="AddressLine1" class="form-label">Address (Line 1) <span
                                    class="text-danger">*</span></label>
                            <input type="text" class="form-control" id="AddressLine1" v-model="form.addressline_1"
                                placeholder="Address (Line 1)" @blur="touched.addressline_1 = true" :disabled="isReadonly">
                            <div v-if="touched.addressline_1 && !form.addressline_1" class="text-danger">
                                Address (Line 1) is required.
                            </div>
                        </div>

                        <div class="col-md-3 mb-3">
                            <label for="Address(Line 2)" class="form-label">Address(Line 2)</label>
                            <input type="text" class="form-control" id="Address(Line 2)" v-model="form.addressline_2"
                                placeholder="Address(Line 2)" :disabled="isReadonly">
                        </div>
                        <div class="col-md-3 mb-3">
                            <label for="Address(Line 3)" class="form-label">Address(Line 3)</label>
                            <input type="text" class="form-control" id="Address(Line 3)" v-model="form.addressline_3"
                                placeholder="Address(Line 3)" :disabled="isReadonly">
                        </div>

                    </div>

                    <!-- <div class="row mt-3">
                    <div class="col-md-3 mb-3">
                        <label for="Country" class="form-label">Country</label>
                        <input type="text" class="form-control" id="Country" v-model="form.country" placeholder="Country">
                    </div>

                    <div class="col-md-3 mb-3">
                        <label for="City" class="form-label">City</label>
                        <input type="text" class="form-control" id="City" v-model="form.city" placeholder="City">
                    </div>

                    <div class="col-md-3 mb-3">
                        <label for="" class="form-label">Region</label>
                        <input type="text" class="form-control" id="Region" v-model="form.region" placeholder="Region">
                    </div>

                    <div class="col-md-3 mb-3">
                        <label for="" class="form-label">Pincode</label>
                        <input type="text" class="form-control" id="Pincode" v-model="form.pincode" placeholder="Pincode">
                    </div>
                </div> -->

                    <div class="row mt-3">
                        <div class="col-md-3 mb-3" :class="{ 'has-error': touched.country && !form.country }">
                            <label for="Country" class="form-label">Country <span class="text-danger">*</span></label>
                            <input type="text" class="form-control" id="Country" v-model="form.country"
                                placeholder="Country" @blur="touched.country = true" :disabled="isReadonly">
                            <div v-if="touched.country && !form.country" class="text-danger">
                                Country is required.
                            </div>
                        </div>

                        <div class="col-md-3 mb-3" :class="{ 'has-error': touched.city && !form.city }">
                            <label for="City" class="form-label">City <span class="text-danger">*</span></label>
                            <input type="text" class="form-control" id="City" v-model="form.city" placeholder="City"
                                @blur="touched.city = true" :disabled="isReadonly">
                            <div v-if="touched.city && !form.city" class="text-danger">
                                City is required.
                            </div>
                        </div>

                        <div class="col-md-3 mb-3" :class="{ 'has-error': touched.region && !form.region }">
                            <label for="Region" class="form-label">State <span class="text-danger">*</span></label>
                            <input type="text" class="form-control" id="Region" v-model="form.region"
                                placeholder="Region" @blur="touched.region = true" :disabled="isReadonly">
                            <div v-if="touched.region && !form.region" class="text-danger">
                                State is required.
                            </div>
                        </div>

                        <div class="col-md-3 mb-3" :class="{ 'has-error': touched.pincode && !form.pincode }">
                            <label for="Pincode" class="form-label">Pincode <span class="text-danger">*</span></label>
                            <input type="text" class="form-control" id="Pincode" v-model="form.pincode"
                                placeholder="Pincode" @blur="touched.pincode = true" :disabled="isReadonly">
                            <div v-if="touched.pincode && !form.pincode" class="text-danger">
                                Pincode is required.
                            </div>
                        </div>

                    </div>

                    <h6 class="mt-3">Residential Details</h6>
                    <div class="row mt-3">
                        <!-- <div class="col-md-6 mb-3">
                        <label for="Residential Status" class="form-label">Residential Status</label>
                        <select name="Residential Status" id="Residential Status" class="form-control" v-model="form.residential_status">
                            <option value="Resident of India">Resident of India</option>
                            <option value="Non-Resident of India">Non-Resident of India</option>
                            <option value="Foreign company having branch in india">Foreign company having branch in india</option>
                        </select>
                    </div> -->


                        <div class="col-md-3 mb-3"
                            :class="{ 'has-error': touched.residential_status && !form.residential_status }">
                            <label for="ResidentialStatus" class="form-label">Residential Status <span
                                    class="text-danger">*</span></label>
                            <select name="ResidentialStatus" id="ResidentialStatus" class="form-control"
                                v-model="form.residential_status" @blur="touched.residential_status = true" :disabled="isReadonly">
                                <option value="">Select Residential Status</option>
                                <option value="Resident of India">Resident of India</option>
                                <option value="Non-Resident of India">Non-Resident of India</option>
                                <option value="Foreign company having branch in india">Foreign company having branch in
                                    India</option>
                            </select>
                            <div v-if="touched.residential_status && !form.residential_status" class="text-danger">
                                Residential Status is required.
                            </div>
                        </div>
                        <div class="col-md-3 mb-3">
                            <label for="TIN" class="form-label">Tax Identification No. (TIN)</label>
                            <input type="text" class="form-control" id="TIN" v-model="form.tax_identification_no_tin"
                                placeholder="TIN No" :disabled="isReadonly">
                        </div>
                        <!-- </div> -->

                        <!-- <div class="row mt-3"> -->
                        <!-- <div class="col-md-4 mb-3">
                        <label for="Permanent Account No." class="form-label">Permanent Account No.</label>
                        <input type="text" class="form-control" id="Permanent Account No." v-model="form.permanent_account_no" placeholder="Permanent Account No.">
                    </div> -->

                        <!-- <div class="col-md-4 mb-3">
                            <label for="Tax Category" class="form-label">Tax Category</label>
                            <select name="tax_category" id="tax_category" class="form-control"
                                v-model="form.tax_category">
                                <option value="Registered Composition">Registered Composition</option>
                                <option value="Reverse Charge Out-State">Reverse Charge Out-State</option>
                                <option value="Reverse Charge In-State">Reverse Charge In-State</option>
                                <option value="Out-State">Out-State</option>
                                <option value="In-State">In-State</option>
                            </select>
                        </div> -->
                        <div class="col-md-3 mb-3">
                            <label for="Tax Category" class="form-label">Tax Category</label>
                            <select class="form-control" id="tax_category" v-model="form.tax_category" :disabled="isReadonly">
                                <option v-for="category in form.taxCategory" :key="category.name"
                                    :value="category.name">
                                    {{ category.name }}
                                </option>
                            </select>
                        </div>

                        <div class="col-md-3 mb-3">
                            <label for="taxWithholdingCategory" class="form-label">Tax Withholding Category</label>
                            <select class="form-control" id="taxWithholdingCategory"
                                v-model="form.tax_withholding_category" :disabled="isReadonly">
                                <option v-for="category in form.taxWithholdingCategories" :key="category.name"
                                    :value="category.name">
                                    {{ category.name }}
                                </option>
                            </select>
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
                                v-model="form.type_of_supplier_under_vat" :disabled="isReadonly">
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
                                placeholder="CST Number" :disabled="isReadonly">
                        </div>
                    </div>

                    <div class="row mt-3">
                        <div class="col-md-4 mb-3">
                            <label for="LST Number" class="form-label">LST Number</label>
                            <input type="text" class="form-control" id="LST Number" v-model="form.lst_number"
                                placeholder="LST Number" :disabled="isReadonly">
                        </div>
                        <!-- <div class="col-md-4 mb-3" :class="{ 'has-error': touched.lst_number && !form.lst_number }">
                            <label for="LSTNumber" class="form-label">LST Number <span
                                    class="text-danger">*</span></label>
                            <input type="text" class="form-control" id="LSTNumber" v-model="form.lst_number"
                                placeholder="LST Number" @blur="touched.lst_number = true">
                            <div v-if="touched.lst_number && !form.lst_number" class="text-danger">
                                LST Number is required.
                            </div>
                    </div> -->

                        <div class="col-md-4 mb-3">
                            <label for="Date for CST" class="form-label">Registration Date for CST</label>
                            <input type="date" class="form-control" id="Date for CST"
                                v-model="form.resistration_date_cst" placeholder="Date for CST" :disabled="isReadonly">
                        </div>

                        <div class="col-md-4 mb-3">
                            <label for="Date for LST" class="form-label">Registration Date for LST</label>
                            <input type="date" class="form-control" id="Date for LST"
                                v-model="form.registration_date_lst" placeholder="Date for LST" :disabled="isReadonly">
                        </div>
                    </div>

                    <h6 class="mt-3">ESI (Employee State Insurance)</h6>
                    <div class="row mt-3">
                        <div class="col-md-6 mb-3">
                            <label for="ESI Number" class="form-label">ESI Number</label>
                            <input type="text" class="form-control" id="ESI Number" v-model="form.esi_number"
                                placeholder="ESI Number" :disabled="isReadonly">
                        </div>
                    </div>

                    <h6 class="mt-3">PF (Provident Fund)</h6>
                    <div class="row mt-3">
                        <div class="col-md-6 mb-3">
                            <label for="EPF Number" class="form-label">EPF Number</label>
                            <input type="text" class="form-control" id="EPF Number" v-model="form.epf_number"
                                placeholder="EPF Number" :disabled="isReadonly">
                        </div>
                    </div>

                    <h6 class="mt-3">MSMED</h6>
                    <div class="row mt-3">
                        <!-- <div class="col-md-3 mb-3">
                        <label for="Enterprise type" class="form-label">Select your Enterprise type</label>
                        <select name="Enterprise type" id="Enterprise type" v-model="form.select_your_enterprise_type" class="form-control">
                            <option value="Micro Enterprise">Micro Enterprise</option>
                            <option value="Small Enterprise">Small Enterprise</option>
                            <option value="Medium Enterprise">Medium Enterprise</option>
                        </select>
                    </div> -->
                        <div class="col-md-3 mb-3">
                            <input type="checkbox" id="msme_applicable" class="form-check-input mr-2"
                                v-model="form.msme_applicable" :disabled="isReadonly">
                            <label for="msme_applicable" class="form-check-label">MSME Applicable</label>
                        </div>

                        <div class="col-md-3 mb-3" v-if="form.msme_applicable">
                            <label for="Certificate Number" class="form-label">MSME/Udyam Registration Number <span
                                class="text-danger">*</span></label>
                            <input type="text" class="form-control" id="Certificate Number"
                                v-model="form.msme_certificate_number" 
                                placeholder="Certificate Number" 
                                :disabled="isReadonly">

                                <!-- <div v-if="touched.msme_certificate_number"
                                class="text-danger">
                               MSME/Udyam Registration Number is required.
                            </div> -->
                        </div>

                        <!-- <div class="col-md-3 mb-3">
                        <label for="Udyam" class="form-label">Udyam Registration Number </label>
                        <input type="text" class="form-control" id="Udyam" placeholder="Udyam" v-model="form.udyam_registration_number">
                    </div> -->

                        <!-- <div class="col-md-3 mb-3"
                            :class="{ 'has-error': touched.udyam_registration_number && !form.udyam_registration_number }">
                            <label for="Udyam" class="form-label">Udyam Registration Number <span
                                    class="text-danger">*</span></label>
                            <input type="text" class="form-control" id="Udyam" v-model="form.udyam_registration_number"
                                placeholder="Udyam" @blur="touched.udyam_registration_number = true">
                            <div v-if="touched.udyam_registration_number && !form.udyam_registration_number"
                                class="text-danger">
                                Udyam Registration Number is required.
                            </div>
                        </div> -->
                    </div>

                    <h6 class="mt-3">WCT</h6>
                    <div class="row mt-3">
                        <div class="col-md-4 mb-3">
                            <label for="Enterprise type" class="form-label">WCT</label>
                            <input type="text" class="form-control" id="WCT" v-model="form.wct" placeholder="WCT" :disabled="isReadonly">
                        </div>
                    </div>
                </div>

            </div>
            
            <div class="d-flex flex-row justify-content-end gap-2 mt-4 mb-3">
                <div v-if="!isReadonly"><button type="button" class="btn btn-primary"  @click="ValidateEmail()" :disabled="!isValid">Save</button></div>
                <div><router-link to="/contactdetails">
                    <button type="button" class="btn btn-primary" >Next</button>
                </router-link></div>
            </div>

        </div>
    </div>

    <!-- Tost Message -->
    <div class="toast align-items-center text-white bg-success  border-0" role="alert" aria-live="assertive"
        aria-atomic="true" :class="{ 'show': showToast }">
        <div class="d-flex">
            <div class="toast-body">
                Details Saved Sucessfully.
            </div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" @click="hideToast"
                aria-label="Close"></button>
        </div>
    </div>
    <!-- Tost Error Message -->
    <div class="toast align-items-center text-white bg-danger  border-0" role="alert" aria-live="assertive"
        aria-atomic="true" :class="{ 'show': showErrorToast }">
        <div class="d-flex">
            <div class="toast-body">
                {{ form.error }}.
            </div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" @click="hideErrorToast"
                aria-label="Close"></button>
        </div>
    </div>
</template>
<script>
import { ref, defineComponent, onMounted, watch, reactive, computed } from "vue";
import { sessionUser } from "../data/session";
import { createResource } from 'frappe-ui';
const showToast = ref(false);
const showErrorToast = ref(false)

function formatDate(dateString) {
    const [day, month, year] = dateString.split('/');
    return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`;
}
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
            company_name: '',
            company_type: '',
            company_registration_number: '',
            small_scale_industries_registration_no: '',
            date_of_establishment: '',
            docname: '',
            nature_of_business: '',
            // d_b_n_d_i_number: '',
            company_turnover: '',
            company_size: '',
            // natl_small_scale_industries_registration_no: '',
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
            gst_status_active: '',
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
            // select_your_enterprise_type: '',
            msme_certificate_number: '',
            udyam_registration_number: '',
            wct: '',
            pan: '',
            taxWithholdingCategories: [],
            taxCategory: [],
            companylist: [],
            msme_applicable: '',
            is_aadhar_pan_linked: 'No',
            // logourl:'',
            legal_name_of_the_business: '',
            constitution_of_business: '',
            address_information_for_principal_place_of_business: '',
            error_message: '',
            gst_error: '',
            error: '',
            applicable_gst:0
        });


        const touched = reactive({
            company_name: false,
            permanent_account_number: false,
            // proprietors_name: false,
            gst_registration_number: false,
            gst_valid_from: false,
            // gst_status: false,
            // gst_status_valid_from: false,
            name_: false,
            addressline_1: false,
            country: false,
            city: false,
            region: false,
            pincode: false,
            residential_status: false,
            tax_identification_no_tin: false,
            permanent_account_no: false,
            // lst_number: false,
            udyam_registration_number: false,
            msme_certificate_number: false,
        });
        const isValid = computed(() => {
            return form.company_name
                // && form.date_of_establishment
                && form.permanent_account_number
                // && form.gst_registration_number
                // && form.gst_status
                && form.name_
                && form.addressline_1
                && form.country
                && form.city
                && form.region
                && form.pincode
                && form.residential_status
            // && form.permanent_account_no
            // && form.lst_number
            // && form.udyam_registration_number;
        });

        const maxDate = ref(new Date().toISOString().split('T')[0]);

        // const isFutureDate = computed(() => {
        //     return form.date_of_establishment > maxDate.value;
        // });
        const isFutureDate1 = computed(() => {
            return form.gst_valid_from > maxDate.value;
        });
        const isFutureDate2 = computed(() => {
            return form.gst_status_valid_from > maxDate.value;
        });

        const loginUser = sessionUser();
        const workflowState = ref('');
        // const isReadonly = computed(() => workflowState.value !== 'Saved');
        const isReadonly = computed(() => {
            return !['Saved', 'Change Requested', 'Approved'].includes(workflowState.value);
        });


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
                    console.log("coming from company details",data)
                    form.company_name = data.company_name;
                    form.company_type = data.company_type;
                    form.company_registration_number = data.company_registration_number;
                    form.small_scale_industries_registration_no = data.small_scale_industries_registration_no;
                    form.date_of_establishment = data.date_of_establishment;
                    form.nature_of_business = data.nature_of_business;
                    // form.d_b_n_d_i_number = data.d_b_n_d_i_number;
                    form.company_turnover = data.company_turnover;
                    form.company_size = data.company_size;
                    // form.natl_small_scale_industries_registration_no = data.natl_small_scale_industries_registration_no;
                    if (data.iso_9001_2000) {
                        form.iso_9001_2000 = true
                    }
                    if (data.iso_4000) {
                        form.iso_4000 = true
                    }
                    if (data.has_18000) {
                        form.has_18000 = true
                    }
                    if (data.any_other_certification) {
                        form.any_other_certification = true
                    }
                    if (data.msme_applicable) {
                        form.msme_applicable = true
                    }
                    if(data.applicable_gst){
                        form.applicable_gst = true
                    }
                    form.permanent_account_number = data.permanent_account_number
                    form.ownership_information = data.ownership_information
                    form.proprietors_name = data.proprietors_name
                    form.gst_registration_number = data.gst_registration_number
                    form.gst_valid_from = data.gst_valid_from
                    form.gst_status = data.gst_status
                    form.gst_status_active = data.gst_status_active
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
                    // form.select_your_enterprise_type = data.select_your_enterprise_type
                    form.msme_certificate_number = data.msme_certificate_number
                    form.udyam_registration_number = data.udyam_registration_number
                    form.wct = data.wct
                    form.is_aadhar_pan_linked = data.is_aadhar_pan_linked
                    // form.logourl = String(data.logo)
                    form.legal_name_of_the_business = data.legal_name_of_the_business
                    form.constitution_of_business = data.constitution_of_business
                    form.address_information_for_principal_place_of_business = data.address_information_for_principal_place_of_business
                    form.docname = data.name
                    workflowState.value = data.workflow_state || '';
                },
                onError: (error) => {
                    console.error('Error:', error);
                }
            });
        });

        const supplier = createResource({
            url: "jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.get_tax_withholding_category",
            makeParams: () => ({}),
            auto: true,
            onSuccess: (data) => {

                form.taxWithholdingCategories = data.taxWithholdingCategories
                form.taxCategory = data.taxCategory
                form.companylist = data.company
            },
            onError: () => {

            }
        })
        const showToastMessage = () => {
            showToast.value = true;
            setTimeout(() => {
                showToast.value = false;
            }, 1000);
        };

        const hideToast = () => {
            showToast.value = false;
        };

        const showErrorToastMessage = (data) => {
            form.error = data
            showErrorToast.value = true;
            setTimeout(() => {
                showErrorToast.value = false;
            }, 1000);
        };

        const hideErrorToast = () => {
            showErrorToast.value = false;
        };


        const ValidateEmail = () => {
            {
                if (form.error_message && form.gst_error) {
                    // alert("PAN & GST number already exists")
                    showErrorToastMessage("PAN & GST number already exists")
                } else if (form.error_message) {
                    // alert("PAN number already exists")
                    showErrorToastMessage("PAN number already exists")
                } else if (form.gst_error) {
                    // alert("GST number already exists")
                    showErrorToastMessage("GST number already exists")
                } else if(form.msme_applicable && !form.msme_certificate_number){
                    showErrorToastMessage("MSME Registration No. required")
                }else if(form.applicable_gst && !form.gst_registration_number){
                    showErrorToastMessage("Gst Registration No. required")
                }else {
                    const supplier = createResource({
                        url: "jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.save_supplier_detail",
                        makeParams: () => ({
                            doc: {
                                company_name: form.company_name,
                                company_type: form.company_type,
                                company_registration_number: form.company_registration_number,
                                small_scale_industries_registration_no: form.small_scale_industries_registration_no,
                                docname: form.docname,
                                date_of_establishment: form.date_of_establishment,
                                nature_of_business: form.nature_of_business,
                                // d_b_n_d_i_number: form.d_b_n_d_i_number,
                                company_turnover: form.company_turnover,
                                company_size: form.company_size,
                                // natl_small_scale_industries_registration_no: form.natl_small_scale_industries_registration_no,
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
                                gst_status_active: form.gst_status_active,
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
                                // select_your_enterprise_type: form.select_your_enterprise_type,
                                msme_certificate_number: form.msme_certificate_number,
                                udyam_registration_number: form.udyam_registration_number,
                                wct: form.wct,
                                msme_applicable: form.msme_applicable,
                                is_aadhar_pan_linked: form.is_aadhar_pan_linked,
                                legal_name_of_the_business: form.legal_name_of_the_business,
                                constitution_of_business: form.constitution_of_business,
                                address_information_for_principal_place_of_business: form.address_information_for_principal_place_of_business
                                // logo : form.logo
                            }
                        }),
                        auto: true,
                        onSuccess: (data) => {
                            showToastMessage()
                        },
                        onError: (error) => {
                            console.error('Error:', error);
                            // alert(`An error occurred: ${error.message}`);
                            showErrorToastMessage("Error Occur while data saving ,Please try again")
                        }
                    });
                }
            }
        };

        watch(() => form.permanent_account_number,
            (newValue, oldValue) => {
                // if(oldValue && newValue!=oldValue){
                if (oldValue != newValue) {
                    form.error_message=''
                    if (newValue && typeof newValue === 'string' && newValue.length >= 4) {
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
                        const fourthChar = newValue[3].toUpperCase();
                        const panType = typeMap[fourthChar];
                        console.log(panType)
                        form.ownership_information = panType
                    }
                    const isDuplicateGstNumber = createResource({
                        url: 'jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.check_pan_number_duplicacy',
                        makeParams: () => ({
                            data: {
                                panNumber: newValue,
                                docname: form.docname,
                            },
                        }),
                        auto: true,
                        onSuccess: (data) => {
                            const isDuplicateGst = data.isDuplicate;

                            if (isDuplicateGst) {
                                console.log("PAN NUMBER ALREADY IN USE, PLEASE SELECT ANOTHER PAN NUMBER");
                                form.error_message="PAN already exist, please use another. "
                            } else {
                                console.log("PAN NUMBER NOT FOUND")
                                try {
                                    const response = createResource({
                                        url: 'jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.get_pan_details',
                                        makeParams: () => ({
                                            data: {
                                                pan: newValue
                                            },
                                        }),
                                        auto: true,
                                        onSuccess: (data) => {
                                            console.log(data)
                                            form.proprietors_name = data.result.name;
                                            const response = createResource({
                                                url: 'jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.is_pan_link_aadhar',
                                                makeParams: () => ({
                                                    data: {
                                                        pan: newValue
                                                    },
                                                }),
                                                auto: true,
                                                onSuccess: (data) => {
                                                    if (data.result.isAadhaarLinked == true) {
                                                        console.log(data.result.isAadhaarLinked)
                                                        form.is_aadhar_pan_linked = "Yes"
                                                    } else {
                                                        form.is_aadhar_pan_linked = "No"
                                                    }
                                                },
                                                onError: (error) => {
                                                    console.log(error)
                                                }
                                            })

                                        }, onError: (error) => {
                                            console.log(error)
                                        }
                                    });
                                } catch (error) {
                                    console.error('Error fetching bank details:', error);
                                }

                                //             const typeMap = {
                                //                 'P': 'Individual',
                                //                 'C': 'Company',
                                //                 'H': 'Hindu Undivided Family',
                                //                 'A': 'Association of Persons',
                                //                 'B': 'Body of Individuals',
                                //                 'G': 'Government Agency',
                                //                 'J': 'Artificial Juridical Person',
                                //                 'L': 'Local Authority',
                                //                 'F': 'Firm/Partnership',
                                //                 'T': 'Trust'
                                //             };
                                //             const fourthChar = newValue.charAt(3).toUpperCase();
                                //             const panType = typeMap[fourthChar];
                                //             console.log(panType)
                                //             form.ownership_information = panType
                            }
                        }
                    });
                }
            });
        watch(() => form.company_turnover,
            (value) => {
                if (value == ">250000000") {
                    form.company_size = "Large Scale"
                } else if (value == ">100000000") {
                    form.company_size = "Mid Scale"
                } else if (value == ">50000000") {
                    form.company_size = "Small Scale"
                } else {
                    form.company_size = "Micro"
                    if (value == "<2000000") {
                        form.gst_status = "Unregistered"
                    }

                }
            })

        watch(() => form.gst_registration_number, (value) => {

            if (value) {
                form.gst_error = ''
                const isDuplicateGstNumber = createResource({
                    url: 'jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.check_gst_number_duplicacy',
                    makeParams: () => ({
                        data: {
                            gstNumber: value,
                            docname: form.docname,
                        },
                    }),
                    auto: true,
                    onSuccess: (data) => {
                        const isDuplicateGst = data.isDuplicate;

                        if (isDuplicateGst) {
                            console.log("GST NUMBER ALREADY IN USE, PLEASE SELECT ANOTHER GST NUMBER");
                            form.gst_error = "GST number alreay in use, please select another ."
                        } else {
                            console.log("GST NUMBER NOT FOUND")
                            try {
                                const response = createResource({
                                    url: 'jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.gst_registration_number',
                                    makeParams: () => ({
                                        data: {
                                            gstNumber: value
                                        },
                                    }),
                                    auto: true,
                                    onSuccess: (data) => {
                                        console.log(data);
                                        // form.gst_valid_from = data.result.rgdt;
                                        const formattedDate = formatDate(data.result.rgdt);

                                        form.gst_valid_from = formattedDate;
                                        const status = data.result.sts;
                                        form.gst_status_active = status === 'Active' ? 'Yes' : 'No';
                                        form.legal_name_of_the_business = data.result.lgnm
                                        form.constitution_of_business = data.result.ctb
                                        form.address_information_for_principal_place_of_business = data.result.pradr.adr
                                        // form.proprietors_name=data.result.tradeNam
                                        // if (data.result.adhrVFlag =="Yes"){
                                        //     form.is_aadhar_pan_linked="Yes"
                                        // }else{
                                        //     form.is_aadhar_pan_linked="No"
                                        // }
                                    },
                                    onError: (error) => {
                                        console.log(error);
                                    }
                                });
                                createResource({
                                    url: 'jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.validate_gstin',
                                    makeParams: () => ({
                                        doc: {
                                            gstin: form.gst_registration_number,
                                            region: form.region
                                        },
                                    }),
                                    auto: true,
                                    onSuccess: (data) => {
                                        console.log(data)
                                        form.gst_status = data
                                    },
                                    onError: (error) => {
                                        console.log(error);
                                    }
                                })
                            }
                            catch (error) {
                                console.error('Error fetching GST registration details:', error);
                            }
                        }
                    }
                });
            }
        });

        // const handleFileChange=(event)=> {
        //     const file = event.target.files[0];
        //     var formData = new FormData();
        //     formData.append('file', file);
        //     formData.append('doctype',"Supplier Clone");
        //     formData.append('docname', form.docname);
        //     formData.append('is_private', 0);  // Change to 1 if the file should be private
        //     formData.append('fieldname',"logo")
        //     formData.append('folder',"Home")
        //     formData.append('attached_to_field',"logo")
        //     fetch('/api/method/upload_file', {
        //         method: 'POST',
        //         body: formData
        //     })
        //     .then(response => response.json())
        //     .then(data => {
        //         console.log(data);
        //         if (data.message) {
        //             var file_url = data.message.file_url;
        //             alert('File uploaded successfully. File URL:', file_url);
        //         }
        //     })
        //     .catch(error => {
        //         console.error('Error uploading file:', error);
        //     });

        //     // reader.readAsBinaryString(file);
        // }
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
            showToast,
            // handleFileChange,
            maxDate,
            // isFutureDate,
            isFutureDate1,
            isFutureDate2,
            showErrorToastMessage,
            showErrorToast,
            hideErrorToast,
            isReadonly
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
    /* font-weight: bolder; */
    margin-left: 0.25rem;
}

.has-error input,
.has-error select {
    border-color: red;
}

/* .has-error label {
    color: red;
} */
:disabled {
    cursor: not-allowed;
}

/* tost css */
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
