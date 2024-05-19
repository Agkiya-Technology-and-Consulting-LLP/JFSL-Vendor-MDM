<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-12">
                <div class="bg-primary text-white p-1 rounded-top">
                    <h5>Company Details</h5>
                </div>

                <div class="row mt-3">
                    <div class="col-md-3 mb-3">
                        <label for="company" class="form-label">Company</label>
                        <input type="text" class="form-control" id="company" placeholder="Company">
                    </div>

                    <div class="col-md-3 mb-3">
                        <label for="companyName" class="form-label">Company Name</label>
                        <input type="text" class="form-control" id="companyName" placeholder="Company Name">
                    </div>

                    <div class="col-md-3 mb-3">
                        <label for="companyType" class="form-label">Company Type</label>
                        <select name="" id="companyType" class="form-control">
                            <option value="M/S">M/S</option>
                        </select>
                    </div>

                    <div class="col-md-3 mb-3">
                        <label for="registrationNumber" class="form-label">Company Registration Number</label>
                        <input type="text" class="form-control" id="registrationNumber" placeholder="Company Number">
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col-md-3 mb-3">
                        <label for="Registration" class="form-label">Small Scale Industries Registration No.</label>
                        <input type="text" class="form-control" id="Registration"
                            placeholder="Small Scale Industries Registration No.">
                    </div>

                    <div class="col-md-3 mb-3">
                        <label for="Establishment" class="form-label">Date Of Establishment</label>
                        <input type="date" class="form-control" id="Establishment" placeholder="Date Of Establishment">
                    </div>

                    <div class="col-md-3 mb-3">
                        <label for="About Company" class="form-label">About Company</label>
                        <input type="text" class="form-control" id="About Company" placeholder="About Company">
                    </div>

                    <div class="col-md-3 mb-3">
                        <label for="D & B-N-D-I Number" class="form-label">D & B-N-D-I Number</label>
                        <input type="text" class="form-control" id="D & B-N-D-I Number"
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
                        <select name="" id="Company Turnover" class="form-control">
                            <option value="">>250000000</option>
                            <option value="">>10000000</option>
                            <option value="">>50000000</option>
                            <option value="">>5000000</option>
                        </select>
                    </div>

                    <div class="col-md-3 mb-3">
                        <label for="Company Size" class="form-label">Company Size</label>
                        <select name="" id="Company Size" class="form-control">
                            <option value="">Large Scale</option>
                            <option value="">>Mid Scale</option>
                            <option value="">Small Scale</option>
                            <option value="">Micro</option>
                        </select>
                    </div>

                    <div class="col-md-3 mb-3">
                        <label for="Small Scale" class="form-label">Natl. Small Scale Industries Rg No.</label>
                        <input type="text" class="form-control" id="Small Scale"
                            placeholder="Small Scale registration no">
                    </div>
                </div>

                <div class="row mt-3">
                    <h6>Certification</h6>
                    <div class="col-md-3 mb-3">
                        <input type="checkbox" class="form-check-input mr-2" id="iso 9001">
                        <label for="iso 9001" class="form-check-label">ISO 9001-2000</label>
                    </div>

                    <div class="col-md-3 mb-3">
                        <input type="checkbox" id="iso 4000" class="form-check-input mr-2">
                        <label for="iso 4000" class="form-check-label">ISO 4000</label>
                    </div>

                    <div class="col-md-3 mb-3">
                        <input type="checkbox" id="HAS 18000" class="form-check-input mr-2">
                        <label for="HAS 18000" class="form-check-label">HAS 18000</label>
                    </div>

                    <div class="col-md-3 mb-3">
                        <input type="checkbox" id="Any" class="form-check-input mr-2">
                        <label for="Any" class="form-check-label">Any other Certification</label>
                    </div>
                </div>

                <div class="bg-primary text-white p-1 rounded-top mt-2">
                    <h5>PAN Details</h5>
                </div>

                <div class="row mt-3">
                    <div class="col-md-4 mb-3">
                        <label for="pan" class="form-label">Permanent account number</label>
                        <input type="text" class="form-control" id="pan" placeholder="Enter PAN No">
                    </div>

                    <div class="col-md-4 mb-3">
                        <label for="Ownership" class="form-label">Ownership information</label>
                        <input type="text" class="form-control" id="Ownership" placeholder="Ownership information">

                    </div>

                    <div class="col-md-4 mb-3">
                        <label for="Proprietor" class="form-label">Proprietor's Name</label>
                        <input type="text" class="form-control" id="Proprietor" placeholder="Proprietor's Name">
                    </div>
                </div>

                <div class="bg-primary text-white p-1 rounded-top mt-2">
                    <h5>GST(Goods & Services )</h5>
                </div>

                <div class="row mt-3">
                    <div class="col-md-6 mb-3">
                        <label for="GST" class="form-label">GST Registration Number</label>
                        <input type="text" class="form-control" id="GST" placeholder="Enter GST No">
                    </div>

                    <div class="col-md-6 mb-3">
                        <label for="valid" class="form-label">GST valid from</label>
                        <input type="date" class="form-control" id="valid">

                    </div>

                    <div class="col-md-6 mb-3">
                        <label for="GST Status" class="form-label">GST Status</label>
                        <input type="text" class="form-control" id="GST Status" placeholder="GST Status">
                    </div>

                    <div class="col-md-6 mb-3">
                        <label for="GST Status " class="form-label">GST Status valid from</label>
                        <input type="date" class="form-control" id="GST Status ">
                    </div>
                </div>

                <div class="bg-primary text-white p-1 rounded-top mt-2">
                    <h5>CIN</h5>
                </div>

                <div class="row mt-3">
                    <div class="col-md-6 mb-3">
                        <label for="CIN" class="form-label">CIN</label>
                        <input type="text" class="form-control" id="CIN" placeholder="Enter CIN No">
                    </div>
                </div>

                <div class="bg-primary text-white p-1 rounded-top mt-2">
                    <h5>Address & Residential Details</h5>
                </div>
                <h6 class="mt-3">Registered Address </h6>
                <div class="row mt-3">
                    <div class="col-md-3 mb-3">
                        <label for="Name" class="form-label">Name</label>
                        <input type="text" class="form-control" id="Name" placeholder="Name">
                    </div>
                    <div class="col-md-3 mb-3">
                        <label for="Address(Line 1)" class="form-label">Address(Line 1)</label>
                        <input type="text" class="form-control" id="Address(Line 1)" placeholder="Address(Line 1)">
                    </div>
                    <div class="col-md-3 mb-3">
                        <label for="Address(Line 2)" class="form-label">Address(Line 2)</label>
                        <input type="text" class="form-control" id="Address(Line 2)" placeholder="Address(Line 2)">
                    </div>
                    <div class="col-md-3 mb-3">
                        <label for="Address(Line 3)" class="form-label">Address(Line 3)</label>
                        <input type="text" class="form-control" id="Address(Line 3)" placeholder="Address(Line 3)">
                    </div>

                </div>

                <div class="row mt-3">
                    <div class="col-md-3 mb-3">
                        <label for="Country" class="form-label">Country</label>
                        <input type="text" class="form-control" id="Country" placeholder="Country">
                    </div>

                    <div class="col-md-3 mb-3">
                        <label for="City" class="form-label">City</label>
                        <input type="text" class="form-control" id="City" placeholder="City">
                    </div>

                    <div class="col-md-3 mb-3">
                        <label for="" class="form-label">Region</label>
                        <input type="text" class="form-control" id="Region" placeholder="Region">
                    </div>

                    <div class="col-md-3 mb-3">
                        <label for="" class="form-label">Pincode</label>
                        <input type="text" class="form-control" id="Pincode" placeholder="Pincode">
                    </div>
                </div>

                <h6 class="mt-3">Residential Details</h6>
                <div class="row mt-3">
                    <div class="col-md-6 mb-3">
                        <label for="Residential Status" class="form-label">Residential Status</label>
                        <select name="Residential Status" id="Residential Status" class="form-control">
                            <option value="">Resident of India</option>
                            <option value="">Non-Resident of India</option>
                            <option value="">Foreign company having branch in india</option>
                        </select>
                    </div>
                    <div class="col-md-6 mb-3">
                        <label for="TIN" class="form-label">Tax Identification No. (TIN)</label>
                        <input type="text" class="form-control" id="TIN" placeholder="TIN No">
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col-md-4 mb-3">
                        <label for="Permanent Account No." class="form-label">Permanent Account No.</label>
                        <input type="text" class="form-control" id="Permanent Account No."
                            placeholder="Permanent Account No.">
                    </div>

                    <div class="col-md-4 mb-3">
                        <label for="Tax Category" class="form-label">Tax Category</label>
                        <input type="text" class="form-control" id="Tax Category" placeholder="Tax Category">
                    </div>

                    <div class="col-md-4 mb-3">
                        <label for="Tax Withholding Category" class="form-label">Tax Withholding Category</label>
                        <input type="text" class="form-control" id="Tax Withholding Category"
                            placeholder="Tax Withholding Category">
                    </div>
                </div>


                <div class="bg-primary text-white p-1 rounded-top mt-2">
                    <h5>Sales Tax, ESI,PF, MSMED And WCT Details</h5>
                </div>

                <h6 class="mt-3">Sales Tax</h6>
                <div class="row mt-3">
                    <div class="col-md-6 mb-3">
                        <label for="Supplier under VAT" class="form-label">Type of Supplier under VAT</label>
                        <select name="Supplier under VAT" id="Supplier under VAT" class="form-control">
                            <option value="">Registered Dealear</option>
                            <option value="">Un-Registered Dealear</option>
                            <option value="">Incentive Unit</option>
                            <option value="">Notified oil company</option>
                            <option value="">SEZ unit</option>
                            <option value="">EQU</option>
                            <option value="">Vendor under threshold unit</option>
                            <option value="">Foriegn Unit</option>
                        </select>
                    </div>
                    <div class="col-md-6 mb-3">
                        <label for="CST Number" class="form-label">CST Number</label>
                        <input type="text" class="form-control" id="CST Number" placeholder="CST Number">
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col-md-4 mb-3">
                        <label for="LST Number" class="form-label">LST Number</label>
                        <input type="text" class="form-control" id="LST Number" placeholder="LST Number">
                    </div>

                    <div class="col-md-4 mb-3">
                        <label for="Date for CST" class="form-label">Registration Date for CST</label>
                        <input type="date" class="form-control" id="Date for CST" placeholder="Date for CST">
                    </div>

                    <div class="col-md-4 mb-3">
                        <label for="Date for LST" class="form-label">Registration Date for LST</label>
                        <input type="date" class="form-control" id="Date for LST" placeholder="Date for LST">
                    </div>
                </div>

                <h6 class="mt-3">ESI (Employee State Insurance)</h6>
                <div class="row mt-3">
                    <div class="col-md-6 mb-3">
                        <label for="ESI Number" class="form-label">ESI Number</label>
                        <input type="text" class="form-control" id="ESI Number" placeholder="ESI Number">
                    </div>
                </div>

                <h6 class="mt-3">PF (Provident Fund)</h6>
                <div class="row mt-3">
                    <div class="col-md-6 mb-3">
                        <label for="EPF Number" class="form-label">EPF Number</label>
                        <input type="text" class="form-control" id="EPF Number" placeholder="EPF Number">
                    </div>
                </div>

                <h6 class="mt-3">MSMED</h6>
                <div class="row mt-3">
                    <div class="col-md-4 mb-3">
                        <label for="Enterprise type" class="form-label">Select your Enterprise type</label>
                        <select name="Enterprise type" id="Enterprise type" class="form-control">
                            <option value="">Micro Enterprise</option>
                            <option value="">Small Enterprise</option>
                            <option value="">Medium Enterprise</option>
                        </select>
                    </div>

                    <div class="col-md-4 mb-3">
                        <label for="Certificate Number" class="form-label">MSME Certificate Number</label>
                        <input type="text" class="form-control" id="Certificate Number"
                            placeholder="Certificate Number">
                    </div>

                    <div class="col-md-4 mb-3">
                        <label for="Udyam" class="form-label">Udyam Registration Number </label>
                        <input type="text" class="form-control" id="Udyam" placeholder="Udyam">
                    </div>
                </div>

                <h6 class="mt-3">WCT</h6>
                <div class="row mt-3">
                    <div class="col-md-4 mb-3">
                        <label for="Enterprise type" class="form-label">WCT</label>
                        <input type="text" class="form-control" id="WCT" placeholder="WCT">
                    </div>
                </div>




            </div>
            <div class="d-flex justify-content-end mt-1 mb-3">
                <Button type="button" class="savebutton">Save</Button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
};
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
label{
    font-weight:600;
}
h6{
    color: #2e6bdc;
    font-weight: bolder;
}
</style>
