from playwright.sync_api import Page
import base64
import os

def drag_and_drop(page:Page, file_path:str, drop_zone_selector: str) -> None:
    with open(file_path, 'rb') as f:
        buffer = f.read()
    pdf_base64 = base64.b64encode(buffer).decode("utf-8")

    # Create the DataTransfer and File
    data_transfer = page.evaluate_handle(
        """
        (data) => {
            const dt = new DataTransfer();
            // Convert the binary string to a hexadecimal string
            const hexString = Uint8Array.from(atob(data), c => c.charCodeAt(0));
            const file = new File([hexString], 'file.pdf', { type: 'application/pdf' });
            dt.items.add(file);
            return dt;
        }
        """, pdf_base64
    )
    # Dispatch the 'drop' event on the target element
    page.dispatch_event(drop_zone_selector, 'drop', {"dataTransfer": data_transfer})

def file_is_loaded(page:Page,type:str,article:str):
    page.locator("h1").get_by_text(f"Get started by uploading your {type} file").is_hidden()
    load_button = page.locator("button").get_by_text(f"Load {article} {type}").is_hidden()

def file_is_not_loaded(page:Page,type:str,article:str):
    page.locator("h1").get_by_text(f"Get started by uploading your {type} file").is_visible()
    load_button = page.locator("button").get_by_text(f"Load {article} {type}")
    load_button.is_visible()
    load_button.is_enabled()

def get_file_path(file_name:str,test_data:str):
    current_working_dir = os.path.abspath(os.path.dirname( __file__ ))
    return os.path.join(current_working_dir+'/..',test_data + file_name)

def verify_upload(page: Page,type:str,file_name):
    type = type.upper()
    # Verify the Application navigated to specific section when clicked on the tab 
    article = 'a'
    if type == "SBOM":
       article = 'an' 
    page.locator("h1").get_by_text(f"Upload {article} {type}").is_visible()
    # Verify the Upload page loaded with input text area with a Load button
    # Verify Load button is visible and enabled
    file_is_not_loaded(page,type,article)
    # Verify user is able to select a file by hovering
    file_path = get_file_path(file_name,'testdata/'+type.lower()+'/') 
    drag_and_drop(page, file_path, "input[type='file']")
    # Verify the input text area loaded with contents
    file_is_loaded(page,type,article)
    monacoEditor = page.locator(".monaco-editor").nth(0)
    monacoEditor.is_visible()
    monacoEditor.click()
    page.keyboard.type('This is a line of text')
    page.get_by_role("alert").get_by_text("Cannot edit in read-only editor").is_visible()
    # Verify Clear button clears the contents on the text area
    page.locator("#file-clear").click()
    file_is_not_loaded(page,type,article)
