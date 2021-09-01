import base64
code = """JycnVGVzdGVyIGZvciBDUzAxJycnDQpmcm9tIHJhbmRvbSBpbXBvcnQgcmFuZGludA0KaW1wb3J0IHVuaXR0ZXN0DQpmcm9tIHVuaXR0ZXN0Lm1vY2sgaW1wb3J0IHBhdGNoDQpmcm9tIGl0ZXJ0b29scyBpbXBvcnQgY2hhaW4NCg0KaW1wb3J0IGNzMDEgYXMgY3MNCg0KZiA9IG9wZW4oJ2RpY3QudHh0JywgJ3InKQ0KbmFtZXMgPSBmLnJlYWRsaW5lcygpDQpmLmNsb3NlKCkNCg0KZGVmIGdlbmVyYXRlX2Vycm9ybWFuY2VyKCk6DQogICAgcmV0dXJuIHJhbmRpbnQoMSw0KSwgcmFuZGludCgxLDMwKQ0KDQpkZWYgdmFsaWRhdGVfZmluZF9oZXJvKGhlcm9lcywgYXR0ciwgc2NvcmUpOg0KICAgIHZhbGlkID0gW10NCiAgICBmb3IgaGVybyBpbiBoZXJvZXM6DQogICAgICAgIGlmIGhlcm9lc1toZXJvXVthdHRyLTFdID49IHNjb3JlOg0KICAgICAgICAgICAgaWYgbm90IGhlcm9lc1toZXJvXVthdHRyLTFdID4gMzA6DQogICAgICAgICAgICAgICAgdmFsaWQuYXBwZW5kKGhlcm8pDQogICAgaWYgdmFsaWQgPT0gW106DQogICAgICAgIHJldHVybiBOb25lDQogICAgcmV0dXJuIHZhbGlkDQoNCmRlZiBsaXN0X21vbnN0ZXJzKGhlcm9lcyk6DQogICAgbW9uc3RlcnMgPSBbXQ0KICAgIGZvciBoZXJvIGluIGhlcm9lczoNCiAgICAgICAgZm9yIGF0dHJpYiBpbiBoZXJvZXNbaGVyb106DQogICAgICAgICAgICBpZiBpbnQoYXR0cmliKSA+PSAzMToNCiAgICAgICAgICAgICAgICBtb25zdGVycy5hcHBlbmQoaGVybykNCiAgICBpZiBtb25zdGVycyA9PSBOb25lOg0KICAgICAgICByZXR1cm4gWzBdDQogICAgcmV0dXJuIG1vbnN0ZXJzDQoNCmRlZiBnZW5fY2hhcigpOg0KICAgIHJldHVybiBuYW1lcy5wb3AocmFuZGludCgxLGxlbihuYW1lcykpLTEpLnJlbW92ZXN1ZmZpeCgnXG4nKSwgW3JhbmRpbnQoMSwzMCksIHJhbmRpbnQoMSwzMCksIHJhbmRpbnQoMSwzMCksIHJhbmRpbnQoMSwzMCldDQoNCmRlZiBtYWtlX2NoYXJfbGlzdChudW1iZXIpOg0KICAgIGNoYXJhY3RlcnMgPSBkaWN0KCkNCiAgICBpZiBudW1iZXIgPCAxOg0KICAgICAgICByZXR1cm4gTm9uZQ0KICAgIGZvciBfIGluIHJhbmdlKG51bWJlcik6DQogICAgICAgIG5hbWUsIHN0YXRzID0gZ2VuX2NoYXIoKQ0KICAgICAgICBjaGFyYWN0ZXJzW25hbWVdID0gc3RhdHMNCiAgICByZXR1cm4gY2hhcmFjdGVycw0KDQpkZWYgY29udmVydF90b19saXN0KGVudHJpZXMpOg0KICAgIGZpbmFsX2xpc3QgPSBbXQ0KICAgIGZvciBlbnRyeSBpbiBlbnRyaWVzOg0KICAgICAgICBzID0gZW50cnkgKyAnLCcgKyAnLCcuam9pbihzdHIoeCkgZm9yIHggaW4gZW50cmllc1tlbnRyeV0pDQogICAgICAgIGZpbmFsX2xpc3QuYXBwZW5kKHMpDQogICAgcmV0dXJuIGZpbmFsX2xpc3QNCg0KIiIiIGhlcm9lcyA9IG1ha2VfY2hhcl9saXN0KDEwKQ0KYXR0ciwgc2NvcmUgPSBnZW5lcmF0ZV9lcnJvcm1hbmNlcigpDQpwcmludCh2YWxpZGF0ZV9maW5kX2hlcm8oaGVyb2VzLCBhdHRyLCBzY29yZSkpDQpjb252ZXJ0X3RvX2xpc3QoaGVyb2VzKSAiIiINCg0KY2xhc3MgVGVzdENvZGVyU2FnYSh1bml0dGVzdC5UZXN0Q2FzZSk6DQogICAgDQogICAgZGVmIF9faW5pdF9fKHNlbGYsICphcmdzLCAqKmt3YXJncyk6DQogICAgICAgIHN1cGVyKFRlc3RDb2RlclNhZ2EsIHNlbGYpLl9faW5pdF9fKCphcmdzLCAqKmt3YXJncykNCg0KICAgICAgICBzZWxmLmhlcm9lc19vbmUgPSBtYWtlX2NoYXJfbGlzdCgxMCkNCiAgICAgICAgc2VsZi5oZXJvZXNfdHdvID0gbWFrZV9jaGFyX2xpc3QoMTApDQogICAgICAgIHNlbGYuaGVyb2VzX3R3by51cGRhdGUoTm90QU1vbnN0ZXIgPSBbMzEsMzEsMzEsMzFdKQ0KICAgICAgICBzZWxmLmhlcm9lc190aHJlZSA9IG1ha2VfY2hhcl9saXN0KDk5OSkNCiAgICAgICAgc2VsZi5oZXJvZXNfZm91ciA9IG1ha2VfY2hhcl9saXN0KDk5OCkNCiAgICAgICAgc2VsZi5oZXJvZXNfZm91ci51cGRhdGUoRGVtb25Mb3JkID0gWzEwMCwgMTAwLCAxMDAsIDEwMF0pDQogICAgICAgIA0KICAgICAgICBzZWxmLmNhc2Vfb25lX2lucHV0ID0gbGlzdChjaGFpbihbJzEwJ10sIGNvbnZlcnRfdG9fbGlzdChzZWxmLmhlcm9lc19vbmUpKSkNCiAgICAgICAgc2VsZi5jYXNlX3R3b19pbnB1dCA9IGxpc3QoY2hhaW4oWycxMSddLCBjb252ZXJ0X3RvX2xpc3Qoc2VsZi5oZXJvZXNfdHdvKSkpDQogICAgICAgIHNlbGYuY2FzZV90aHJlZV9pbnB1dCA9IGxpc3QoY2hhaW4oWyc5OTknXSwgY29udmVydF90b19saXN0KHNlbGYuaGVyb2VzX3RocmVlKSkpDQogICAgICAgIHNlbGYuY2FzZV9mb3VyX2lucHV0ID0gbGlzdChjaGFpbihbJzk5OSddLCBjb252ZXJ0X3RvX2xpc3Qoc2VsZi5oZXJvZXNfZm91cikpKQ0KDQogICAgICAgIHNlbGYuY2FzZV9vbmVfYXR0ciwgc2VsZi5jYXNlX29uZV9zY29yZSA9IGdlbmVyYXRlX2Vycm9ybWFuY2VyKCkNCiAgICAgICAgc2VsZi5jYXNlX3R3b19hdHRyLCBzZWxmLmNhc2VfdHdvX3Njb3JlID0gZ2VuZXJhdGVfZXJyb3JtYW5jZXIoKQ0KICAgICAgICBzZWxmLmNhc2VfdGhyZWVfYXR0ciwgc2VsZi5jYXNlX3RocmVlX3Njb3JlID0gZ2VuZXJhdGVfZXJyb3JtYW5jZXIoKQ0KICAgICAgICBzZWxmLmNhc2VfZm91cl9hdHRyLCBzZWxmLmNhc2VfZm91cl9zY29yZSA9IGdlbmVyYXRlX2Vycm9ybWFuY2VyKCkNCg0KICAgIGRlZiB0ZXN0X29uZShzZWxmKToNCiAgICAgICAgd2l0aCBwYXRjaCgnYnVpbHRpbnMuaW5wdXQnLCBzaWRlX2VmZmVjdD1zZWxmLmNhc2Vfb25lX2lucHV0KToNCiAgICAgICAgICAgIGFucyA9IGNzLmZpbmRfaGVybyhzZWxmLmNhc2Vfb25lX2F0dHIsIHNlbGYuY2FzZV9vbmVfc2NvcmUpDQogICAgICAgICAgICBtb25zdGVycyA9IGxpc3RfbW9uc3RlcnMoc2VsZi5oZXJvZXNfb25lKQ0KICAgICAgICAgICAgc2VsZi5hc3NlcnRFcXVhbChhbnMsIHZhbGlkYXRlX2ZpbmRfaGVybyhzZWxmLmhlcm9lc19vbmUsIHNlbGYuY2FzZV9vbmVfYXR0ciwgc2VsZi5jYXNlX29uZV9zY29yZSkpDQogICAgICAgICAgICBpZiBhbGwoW2FucyAhPSBOb25lLCB2YWxpZGF0ZV9maW5kX2hlcm8oc2VsZi5oZXJvZXNfb25lLCBzZWxmLmNhc2Vfb25lX2F0dHIsIHNlbGYuY2FzZV9vbmVfc2NvcmUpICE9IE5vbmVdKToNCiAgICAgICAgICAgICAgICBzZWxmLmFzc2VydEVxdWFsKGFueSh4IGluIG1vbnN0ZXJzIGZvciB4IGluIGFucyksIEZhbHNlKQ0KDQogICAgZGVmIHRlc3RfdHdvKHNlbGYpOg0KICAgICAgICB3aXRoIHBhdGNoKCdidWlsdGlucy5pbnB1dCcsIHNpZGVfZWZmZWN0PXNlbGYuY2FzZV90d29faW5wdXQpOg0KICAgICAgICAgICAgYW5zID0gY3MuZmluZF9oZXJvKHNlbGYuY2FzZV90d29fYXR0ciwgc2VsZi5jYXNlX3R3b19zY29yZSkNCiAgICAgICAgICAgIG1vbnN0ZXJzID0gbGlzdF9tb25zdGVycyhzZWxmLmhlcm9lc190d28pDQogICAgICAgICAgICBzZWxmLmFzc2VydEVxdWFsKGFucywgdmFsaWRhdGVfZmluZF9oZXJvKHNlbGYuaGVyb2VzX3R3bywgc2VsZi5jYXNlX3R3b19hdHRyLCBzZWxmLmNhc2VfdHdvX3Njb3JlKSkNCiAgICAgICAgICAgIGlmIGFsbChbYW5zICE9IE5vbmUsIHZhbGlkYXRlX2ZpbmRfaGVybyhzZWxmLmhlcm9lc190d28sIHNlbGYuY2FzZV90d29fYXR0ciwgc2VsZi5jYXNlX3R3b19zY29yZSkgIT0gTm9uZV0pOg0KICAgICAgICAgICAgICAgIHNlbGYuYXNzZXJ0RXF1YWwoYW55KHggaW4gbW9uc3RlcnMgZm9yIHggaW4gYW5zKSwgRmFsc2UpDQogICAgDQogICAgZGVmIHRlc3RfdGhyZWUoc2VsZik6DQogICAgICAgIHdpdGggcGF0Y2goJ2J1aWx0aW5zLmlucHV0Jywgc2lkZV9lZmZlY3Q9c2VsZi5jYXNlX3RocmVlX2lucHV0KToNCiAgICAgICAgICAgIGFucyA9IGNzLmZpbmRfaGVybyhzZWxmLmNhc2VfdGhyZWVfYXR0ciwgc2VsZi5jYXNlX3RocmVlX3Njb3JlKQ0KICAgICAgICAgICAgbW9uc3RlcnMgPSBsaXN0X21vbnN0ZXJzKHNlbGYuaGVyb2VzX3RocmVlKQ0KICAgICAgICAgICAgc2VsZi5hc3NlcnRFcXVhbChhbnMsIHZhbGlkYXRlX2ZpbmRfaGVybyhzZWxmLmhlcm9lc190aHJlZSwgc2VsZi5jYXNlX3RocmVlX2F0dHIsIHNlbGYuY2FzZV90aHJlZV9zY29yZSkpDQogICAgICAgICAgICBpZiBhbGwoW2FucyAhPSBOb25lLCB2YWxpZGF0ZV9maW5kX2hlcm8oc2VsZi5oZXJvZXNfdGhyZWUsIHNlbGYuY2FzZV90aHJlZV9hdHRyLCBzZWxmLmNhc2VfdGhyZWVfc2NvcmUpICE9IE5vbmVdKToNCiAgICAgICAgICAgICAgICBzZWxmLmFzc2VydEVxdWFsKGFueSh4IGluIG1vbnN0ZXJzIGZvciB4IGluIGFucyksIEZhbHNlKQ0KDQogICAgZGVmIHRlc3RfZm91cihzZWxmKToNCiAgICAgICAgd2l0aCBwYXRjaCgnYnVpbHRpbnMuaW5wdXQnLCBzaWRlX2VmZmVjdD1zZWxmLmNhc2VfZm91cl9pbnB1dCk6DQogICAgICAgICAgICBhbnMgPSBjcy5maW5kX2hlcm8oc2VsZi5jYXNlX2ZvdXJfYXR0ciwgc2VsZi5jYXNlX2ZvdXJfc2NvcmUpDQogICAgICAgICAgICBtb25zdGVycyA9IGxpc3RfbW9uc3RlcnMoc2VsZi5oZXJvZXNfZm91cikNCiAgICAgICAgICAgIHNlbGYuYXNzZXJ0RXF1YWwoYW5zLCB2YWxpZGF0ZV9maW5kX2hlcm8oc2VsZi5oZXJvZXNfZm91ciwgc2VsZi5jYXNlX2ZvdXJfYXR0ciwgc2VsZi5jYXNlX2ZvdXJfc2NvcmUpKQ0KICAgICAgICAgICAgaWYgYWxsKFthbnMgIT0gTm9uZSwgdmFsaWRhdGVfZmluZF9oZXJvKHNlbGYuaGVyb2VzX2ZvdXIsIHNlbGYuY2FzZV9mb3VyX2F0dHIsIHNlbGYuY2FzZV9mb3VyX3Njb3JlKSAhPSBOb25lXSk6DQogICAgICAgICAgICAgICAgc2VsZi5hc3NlcnRFcXVhbChhbnkoeCBpbiBtb25zdGVycyBmb3IgeCBpbiBhbnMpLCBGYWxzZSkNCg0KaWYgX19uYW1lX18gPT0gJ19fbWFpbl9fJzoNCiAgICB1bml0dGVzdC5tYWluKCk="""
eval(compile(base64.b64decode(code), '<string>', 'exec'))