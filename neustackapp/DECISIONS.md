DECISIONS.md
============

Decision 1: Use In-Memory Storage Instead of a Database
=======================================================

Context
-------

The assignment explicitly states that a database is not required and that an in-memory store is acceptable.

### Options Considered

*   Option A: PostgreSQL or SQLite database.
    
*   Option B: Python in-memory dictionaries and lists.
    

### Choice

Used Python dictionaries and lists as the application's data store.

### Why

The primary goal of the assignment is to demonstrate API design and business logic rather than database modeling. Using an in-memory store keeps the implementation lightweight and allows focus on checkout flows, coupon generation, and reporting logic.

If the application needed persistence in production, repositories could be backed by PostgreSQL or Redis with minimal service layer changes.

Decision 2: Introduce a Service Layer
=====================================

Context
-------

Business logic such as checkout, coupon validation, and report generation can either be implemented directly inside API views or separated into dedicated services.

### Options Considered

*   Option A: Place business logic inside Django APIViews.
    
*   Option B: Create dedicated service classes.
    

### Choice

Implemented separate service classes.

### Why

Separating business logic from API views provides:

*   Better readability.
    
*   Easier unit testing.
    
*   Reusability.
    
*   Reduced view complexity.
    

The views remain responsible only for request validation and response generation.

Decision 3: Use a Repository Layer
==================================

Context
-------

Application data is stored in memory, but direct access to global dictionaries from multiple modules can tightly couple business logic to storage implementation.

### Options Considered

*   Option A: Access global dictionaries directly.
    
*   Option B: Introduce repository classes.
    

### Choice

Used repository modules to manage application state.

### Why

Repositories provide an abstraction layer between storage and business logic.

This design allows future migration to:

*   PostgreSQL.
    
*   Redis.
    
*   External services.
    

without modifying the service layer.

Decision 4: Protect Checkout Logic Using Locks
==============================================

Context
-------

The discount system awards every nth order with a coupon code.

Concurrent requests may result in multiple requests receiving the same nth-order reward.

### Options Considered

*   Option A: No synchronization.
    
*   Option B: Use thread synchronization.
    

### Choice

Used Python's threading.Lock during order creation.

### Why

Without synchronization:

*   Two concurrent requests may both observe the same order count.
    
*   Duplicate coupon generation may occur.
    

The lock guarantees that order counting and coupon generation remain consistent.

Although the application currently runs in memory, this design consideration demonstrates awareness of concurrency issues.

Decision 5: Coupons Are Single Use
==================================

Context
-------

The assignment does not explicitly define coupon reuse behavior.

### Options Considered

*   Option A: Allow unlimited usage.
    
*   Option B: Allow a single usage.
    

### Choice

Coupons become invalid after successful application.

### Why

Single-use coupons prevent abuse and simplify business rules.

This behavior also matches common ecommerce implementations where promotional codes are redeemed once.

Decision 6: Generate UUID-Based Order IDs
=========================================

Context
-------

Each order requires a unique identifier.

### Options Considered

*   Option A: Sequential numeric IDs.
    
*   Option B: UUIDs.
    

### Choice

Used UUIDs for order identifiers.

### Why

UUIDs provide:

*   Global uniqueness.
    
*   No dependency on a database sequence.
    
*   Reduced predictability.
    

This approach is common in distributed systems.

Decision 7: Validate Requests Using DRF Serializers
===================================================

Context
-------

Incoming API requests require validation.

### Options Considered

*   Option A: Manual validation inside views.
    
*   Option B: Django REST Framework serializers.
    

### Choice

Used DRF serializers.

### Why

Serializers provide:

*   Centralized validation.
    
*   Automatic error responses.
    
*   Cleaner API views.
    
*   Better maintainability.
    

Validation rules such as minimum quantity and positive prices are enforced consistently.