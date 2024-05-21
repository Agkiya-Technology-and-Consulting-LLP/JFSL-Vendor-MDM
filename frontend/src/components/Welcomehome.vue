<template>
    <div class="w-full h-auto shadow-2xl rounded p-4">

        <div class="content">
            <h2 class="text-gray-700">Welcome</h2>
            <p class="text-gray-700">Setup your Reliance Supplier account with few simple steps</p>
        </div>
        <hr>

        <div class="boxes d-flex justify-between mt-12">

            <router-link to="./companydetails" class="no-underline">
                <div class="w-48">
                    <div class="d-flex flex-col w-48 h-48 border-dashed border-1 border-gray-500 rounded p-2">
                        <span class="text-white bg-gray-500 w-14 p-0.5 rounded"><small>Pending</small></span>
                        <i class="h-16 mt-6 text-blue-500 fa-regular fa-building"></i>
                        <h5 class="text-blue-500 text-center mt-4">Company Details</h5>
                    </div>
                    <p class="text-center text-gray-700 font-medium"><small>Update your company information, logo and
                            product/service offerings</small></p>
                </div>
            </router-link>

            <router-link to="./Categorybusiness" class="no-underline">
                <div class="w-48">
                    <div class="d-flex flex-col w-48 h-48 border-dashed border-1 border-gray-500 rounded p-2">
                        <span class="text-white bg-gray-500 w-14 p-0.5 rounded"><small>Pending</small></span>
                        <i class="h-16 mt-6 text-blue-500 fa-solid fa-business-time"></i>
                        <h5 class="text-blue-500 text-center mt-4">Supplier Details</h5>
                    </div>
                    <p class="text-center text-gray-700 font-medium"><small>Update your Supplier information</small></p>
                </div>
            </router-link>

            <router-link to="./contactdetails" class="no-underline">
                <div class="w-48">
                    <div class="d-flex flex-col w-48 h-48 border-dashed border-1 border-gray-500 rounded p-2">
                        <span class="text-white bg-gray-500 w-14 p-0.5 rounded"><small>Pending</small></span>
                        <i class="h-16 mt-6 text-blue-500 fa-regular fa-address-book"></i>
                        <h5 class="text-blue-500 text-center mt-4">Contact Details</h5>
                    </div>
                    <p class="text-center text-gray-700 font-medium"><small>Add Owner details and import your employee
                            data</small></p>
                </div>
            </router-link>

            <router-link to="./accountdetails" class="no-underline">
                <div class="w-48">
                    <div class="d-flex flex-col w-48 h-48 border-dashed border-1 border-gray-500 rounded p-2">
                        <span class="text-white bg-gray-500 w-14 p-0.5 rounded"><small>Pending</small></span>
                        <i class="h-16 mt-6 text-blue-500 fa-solid fa-receipt"></i>
                        <h5 class="text-blue-500 text-center mt-4">Account Details</h5>
                    </div>
                    <p class="text-center text-gray-700 font-medium"><small>Add account details</small></p>
                </div>
            </router-link>

            <router-link to="./documentdetails" class="no-underline">
                <div class="w-48">
                    <div class="d-flex flex-col w-48 h-48 border-dashed border-1 border-gray-500 rounded p-2">
                        <span class="text-white bg-gray-500 w-14 p-0.5 rounded"><small>Pending</small></span>
                        <i class="h-16 mt-6 text-blue-500 fa-solid fa-folder-open"></i>
                        <h5 class="text-blue-500 text-center mt-4">Document</h5>
                    </div>
                    <p class="text-center text-gray-700 font-medium"><small>Add and upload your verification documents
                            in the portal</small></p>
                </div>
            </router-link>

        </div>

        <div class="action d-flex justify-end mt-10">
            <router-link to="./companydetails" class="no-underline">
            <button class="text-white bg-blue-500 p-2 rounded ">Get Started</button>
        </router-link>
        </div>

    </div>
</template>
<style scoped>
@media only screen and (max-width: 480px) {
    .boxes{
       display: flex;
       flex-direction: column;
       align-items: center;
    }
}
</style>